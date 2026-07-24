# TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder

**Framework**: Technotes

Update existing code for two foundational changes in SwiftUI built with Xcode 27.

#### Overview

SwiftUI in Xcode 27 introduces two changes to the language-level shape of the framework:

- **[`State`](https://developer.apple.com/documentation/SwiftUI/State) is a Swift macro rather than a property wrapper.** The macro enables lazy evaluation of a property’s initial value, and the compiler treats the property like any other stored property of the view.
- **Result builders are unified under [`ContentBuilder`](https://developer.apple.com/documentation/SwiftUI/ContentBuilder).** In order to drastically improve typechecking performance, previously distinct builders such as [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) are unified under `@ContentBuilder`, and builder blocks no longer carry specific protocol constraints on their contents, drastically improving typechecking performance.

The vast majority of SwiftUI code in your app is unaffected and continues to compile and behave the same way without modification. A small number of patterns that depended on the previous implementations now produce build errors. The following sections describe each known source incompatibility, the recommended remediation, and the underlying cause.

To locate a specific build error, see the [`Diagnostic reference`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Diagnostic-reference.md) at the end of this document.

#### Understanding the Changes

Before diving into specific errors, it helps to understand what changed and why. Both changes were made to target specific developer pain-points, but share a common theme that causes source incompatibility: the compiler now has different information about your code, meaning some code that compiled before is now unsupported.

##### How State Evolved to Support Laziness

Previously, when you wrote a state variable, that state value would be recreated every time its containing view was initialized. In SwiftUI, views are intended to be lightweight values that are created frequently, and so views and their contained state values are recreated frequently.

This behavior is fine when the state contains value types, but reference types must heap allocate every time they’re instantiated, meaning this recreation causes performance degradations, or unintended work to initialize these objects.

By making `@State` a macro, SwiftUI can ensure that objects held in state are only ever initialized one time, when the view is first created, avoiding this performance issue.

##### How Result Builders Changed to Be Unified Under Contentbuilder

SwiftUI previously defined a separate result builder for each kind of content you compose. Every primitive those builders share, such as [`Group`](https://developer.apple.com/documentation/SwiftUI/Group), [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach), and [`Section`](https://developer.apple.com/documentation/SwiftUI/Section), provided a separate initializer for each builder. Because these initializers differ only in the type of content the builder produces, and that type doesn’t appear at the call site, the compiler infers which initializer to use.

Inferring the initializer requires typechecking the entire closure body. When that body contains more overloaded primitives, the compiler repeats this work for each candidate while keeping its choices consistent across the closure. The cost grows quickly as builders nest, and deeply nested uses of `Group`, `Section`, or `ForEach` can exceed the compiler’s limits, producing the error:

```None
the compiler is unable to type-check this expression in reasonable time
```

[`ContentBuilder`](https://developer.apple.com/documentation/SwiftUI/ContentBuilder) replaces these builders with a single builder that imposes no constraints on its contents. It assembles arbitrary content, and that content conforms to the protocol its context requires only when its elements do. Each primitive provides one builder-based initializer, so the compiler no longer searches indistinguishable overloads or typechecks closure bodies to choose one. Your code keeps the same syntax and type safety, and typechecks substantially faster.

#### Migrating Code That Uses State

`@State` now participates in initialization the same way any stored property does, meaning the compiler now diagnoses several patterns that were previously accepted, but never well-defined.

The content within this section covers these patterns that no longer compile.

##### Initialize Stored Properties Before Assigning to State in Init

**What happens:** A view whose `init` assigns to a `@State` property before all other stored properties have been initialized produces one of the following diagnostics:

```None
error: 'self' used in property access '_counter' before 'super.init' call
error: variable 'self.counter' used before being initialized
```

The following code reproduces the error:

```swift
import SwiftUI

struct ContentView: View {
    var name: String
    @State private var counter: Int

    init(name: String) {
        self.counter = 42
        self.name = name
    }

    var body: some View { Text("\(name): \(counter)") }
}
```

**How to fix it:** Initialize all non-`@State` stored properties before assigning to any `@State` property.

**Why this occurs:** The `@State` macro synthesizes a backing storage property, `_counter` in the example above. Assigning to this property before the remainder of `self` is initialized is a use of `self` prior to full initialization, which the compiler now reports. This pattern arises when a view’s initial state must be derived from a value passed to its initializer.

> ❗ **Important**: Assigning to a `@State` property that already has an inline initial value is not supported and does not produce the expected behavior at runtime. The inline initial value takes precedence, and any value assigned in `init` is discarded. For example, the following view observes `counter` as `0` in its body: ```swift
struct ContentView: View {
    @State private var counter: Int = 0

    init() {
        self.counter = 42
    }
}
``` When the initial value of a `@State` property must be supplied by the initializer, omit the inline default: ```swift
struct ContentView: View {
    @State private var counter: Int

    init() {
        self.counter = 42
    }
}
```

##### Avoid Composing Additional Property Wrappers with State

**What happens:** Applying another property wrapper to a property declared with `@State` produces:

```None
error: invalid redeclaration of synthesized property '_counter'
```

**How to fix it:** Remove the additional property wrapper.

**Why this occurs:** The composed property wrapper and the `@State` macro each attempt to synthesize a backing storage property using the same underscore-prefixed name.

##### Define Memberwise Initializers Explicitly When a View Has Private State

**What happens:** In Swift, a type whose stored properties are all `private` and that does not declare an explicit initializer receives a synthesized memberwise initializer with `private` access, callable from initializers defined in extensions of the type. Views that declare a `@State` property no longer receive this synthesized initializer, and call sites in extensions fail to resolve:

```swift
struct Foo: View {
    @State private var bar = 0
    private let baz: Int
}

extension Foo {
    init(_ bar: Int, baz: Int) {
        self.init(bar: bar, baz: baz) // error: no exact matches in call to initializer
    }
}
```

**How to fix it:** Define the memberwise initializer explicitly rather than relying on synthesis.

**Why this occurs:** The expansion of the `@State` macro causes the compiler to skip synthesis of the memberwise initializer, per [`Init Accessors`](https://developer.apple.comhttps://github.com/swiftlang/swift-evolution/blob/main/proposals/0400-init-accessors.md).

#### Migrating Code That Uses Result Builders

Many of SwiftUI’s result builders are unified under `@ContentBuilder`, improving typechecking performance. To accomplish this, the constraint that previously required builder block contents to conform to `View` has been removed. This change causes a few source incompatibilities, most of which relate to no longer being able to use that view constraint to choose between otherwise ambiguous overloads.

##### Use the Closure Based Forms of Background and Overlay for Shapestyle Expressions

**What happens:** A call to the deprecated, non-builder forms of [`background(alignment:content:)`](https://developer.apple.com/documentation/SwiftUI/View/background(alignment:content:)) or [`overlay(alignment:content:)`](https://developer.apple.com/documentation/SwiftUI/View/overlay(alignment:content:)) that passes a [`ShapeStyle`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle) expression composed with modifiers such as [`opacity(_:)`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle/opacity(_:)-swift.type.method) or [`blendMode(_:)`](https://developer.apple.com/documentation/SwiftUI/ShapeStyle/blendMode(_:)-swift.type.method) produces:

```None
error: ambiguous use of 'opacity'
error: ambiguous use of 'blendMode'
```

The following code reproduces the error:

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Text("Hello")
            .overlay(Color.blue.opacity(0.70).blendMode(.overlay))
    }
}
```

**How to fix it:** Use the closure-based form of `background(_:)` or `overlay(_:)`:

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Rectangle()
            .overlay { Color.blue.opacity(0.3).blendMode(.overlay) }
    }
}
```

**Why this occurs:** Both `background` and `overlay` provide overloads that accept either a `View` or a `ShapeStyle`, and modifiers such as `opacity(_:)` on a `ShapeStyle` return either a `ShapeStyle` or a `View`. The `View` constraint that [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) previously imposed allowed the compiler to select a single resolution for these expressions. Without that constraint, the competing overloads are equally viable and the expression becomes ambiguous. The closure-based form selects the builder overload directly and resolves the ambiguity.

##### Disambiguate Types and Members That Collide Across Modules

**What happens:** If a project imports a module that declares a type whose name matches a SwiftUI type, or a type with members that match those of a SwiftUI type, the compiler may report an ambiguity at the use site. This applies to any duplicated type, such as a framework’s own `Text` declaration whose overloads match those of SwiftUI’s `Text`, and to any duplicated static member of such a type, such as `red`, `green`, `blue`, or `clear`.

For example, when a project imports a module that declares its own `Color` type with a `clear` member, the compiler produces:

```None
error: ambiguous use of 'clear'
```

The following code reproduces the error:

```swift
// In MyPackage:
public struct Color {
    public static let clear = Color()
}

// In the app:
import SwiftUI
import MyPackage

struct ContentView: View {
    var body: some View {
        Color.clear
    }
}
```

**How to fix it:** Fully qualify the type with its module name, or rename the conflicting type or member in the other module.

```swift
import SwiftUI
import MyPackage

struct ContentView: View {
    var body: some View {
        SwiftUI.Color.clear
    }
}
```

**Why this occurs:** The `View` constraint on `@ViewBuilder` previously allowed the compiler to exclude non-`View`-conforming candidates during overload resolution. With the constraint removed, both candidates are equally valid and the compiler reports the ambiguity.

##### Update Generic Constraints That Reference Tupleview

**What happens:** Code that names [`TupleView`](https://developer.apple.com/documentation/SwiftUI/TupleView) as a nested generic type argument may produce one of the following diagnostics:

```None
error: cannot convert value of type 'VStack<TupleContent<Text, Text>>' to expected argument type 'VStack<TupleView<(Text, Text)>>'

error: cannot convert value of type 'Label<TupleContent<Text, Text?>, Image?>' to expected argument type 'Label<TupleView<(Text, Optional<Text>)>, Optional<Image>>'
```

The following code reproduces the error:

```swift
import SwiftUI

struct CardView<Content: View>: View {
    var content: Content
    var body: some View { content }
    init(@ContentBuilder content: () -> Content) {
        self.content = content()
    }
}

extension CardView where Content == VStack<TupleView<(Text, Text)>> {
    init(title: String, subtitle: String) {
        self = CardView {
            VStack {
                Text(title)
                Text(subtitle)
            }
        }
    }
}
```

**How to fix it:** Prefer opaque types such as `some View` rather than spelling the concrete builder return type. When a concrete spelling is required, replace `TupleView` with [`TupleContent`](https://developer.apple.com/documentation/SwiftUI/TupleContent) in the constraint:

```swift
extension CardView where Content == VStack<TupleContent<Text, Text>> {
    init(title: String, subtitle: String) {
        self = CardView {
            VStack {
                Text(title)
                Text(subtitle)
            }
        }
    }
}
```

For projects with a minimum deployment target earlier than iOS 27, iPadOS 27, macOS 27, or visionOS 27, where `TupleContent` is unavailable, retain the `TupleView` constraint and construct the `TupleView` explicitly inside the builder:

```swift
extension CardView where Content == VStack<TupleView<(Text, Text)>> {
    init(title: String, subtitle: String) {
        self = CardView {
            VStack {
                TupleView((
                    Text(title),
                    Text(subtitle)
                ))
            }
        }
    }
}
```

**Why this occurs:** The unified `@ContentBuilder` produces `TupleContent` rather than `TupleView` as the concrete return type for multi-expression builder blocks. When `TupleView` appears as a nested generic argument, the contextual type does not propagate deeply enough to redirect the inner builder’s return type, and the resulting type does not match the declared constraint.

##### Provide an Explicit Empty Content Value in Nested Builders When Mapkit Is in Scope

**What happens:** When SwiftUI and MapKit are both in scope in a source file, an empty result builder block — including a conditional compilation block whose only branch is excluded — within a nested builder produces:

```None
error: return type of property 'body' requires that 'EmptyMapContent' conform to 'View'
```

> **Note**: This diagnostic can occur in source files that do not explicitly import MapKit when the project does not enable member import visibility. Do not rule out this diagnostic based solely on the imports declared in the file.

The following code reproduces the error:

```swift
import SwiftUI
import MapKit

struct ContentView: View {
    var body: some View {
        Group { }
    }
}
```

The same error occurs when a conditional compilation block resolves to an empty body — for example, when the active configuration causes the only branch to be excluded:

```swift
import SwiftUI
import MapKit

struct ContentView: View {
    var body: some View {
        Group {
            #if MY_CONDITION
            MyView()
            #endif
        }
    }
}
```

**How to fix it:** Supply an explicit [`EmptyContent`](https://developer.apple.com/documentation/SwiftUI/EmptyContent) (or [`EmptyView`](https://developer.apple.com/documentation/SwiftUI/EmptyView)) value:

```swift
import SwiftUI
import MapKit

struct ContentView: View {
    var body: some View {
        Group {
            EmptyContent()
        }
    }
}
```

For the conditional compilation case, add an `#else` branch that produces an explicit `EmptyContent()` (or `EmptyView()`):

```swift
import SwiftUI
import MapKit

struct ContentView: View {
    var body: some View {
        Group {
            #if MY_CONDITION
            MyView()
            #else
            EmptyContent()
            #endif
        }
    }
}
```

**Why this occurs:** Without the `View` constraint on the builder, an empty body is ambiguous when MapKit is also in scope: MapKit declares its own result builder that produces [`EmptyMapContent`](https://developer.apple.com/documentation/MapKit/EmptyMapContent), and the compiler has no basis to choose between the two. Supplying an explicit `EmptyContent()` (or `EmptyView()`) anchors the resolution to a concrete `View`-conforming expression.

##### Extract Deeply Branching Content From Chart Closures When Back Deploying

**What happens:** For projects whose minimum deployment target is earlier than iOS 27, iPadOS 27, macOS 27, or visionOS 27, a [`Chart`](https://developer.apple.com/documentation/Charts/Chart) that contains deeply branching `if` / `else if` or `switch` statements may produce:

```None
error: the compiler is unable to type-check this expression in reasonable time
```

This diagnostic does not occur in projects whose minimum deployment target is iOS 27, iPadOS 27, macOS 27, or visionOS 27. The threshold for the diagnostic is approximately ten or more branches.

The following code reproduces the error:

```swift
import SwiftUI
import Charts

struct DataPoint {
    var index: Int
    var rate: Double
    var signal: Double
    var noise: Double
    var errors: Double
    var throughput: Double
    var txRate: Double
    var rxRate: Double
    var txFrames: Double
    var rxFrames: Double
    var channel: Double
    var bandwidth: Double
    var defaultValue: Double
}

struct MetricChartView: View {
    var selectedMetric: String
    var dataPoints: [DataPoint]

    var body: some View {
        Chart(dataPoints, id: \.index) { dataPoint in
            if selectedMetric == "Rate" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rate))
                    .foregroundStyle(.blue)
            } else if selectedMetric == "Signal" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.signal))
                    .foregroundStyle(.green)
            } else if selectedMetric == "Noise" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.noise))
                    .foregroundStyle(.red)
            } else if selectedMetric == "Errors" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.errors))
                    .foregroundStyle(.orange)
            } else if selectedMetric == "Throughput" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.throughput))
                    .foregroundStyle(.purple)
            } else if selectedMetric == "TX Rate" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.txRate))
                    .foregroundStyle(.cyan)
            } else if selectedMetric == "RX Rate" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rxRate))
                    .foregroundStyle(.mint)
            } else if selectedMetric == "TX Frames" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.txFrames))
                    .foregroundStyle(.indigo)
            } else if selectedMetric == "RX Frames" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rxFrames))
                    .foregroundStyle(.brown)
            } else if selectedMetric == "Channel" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.channel))
                    .foregroundStyle(.teal)
            } else if selectedMetric == "Bandwidth" {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.bandwidth))
                    .foregroundStyle(.pink)
            } else {
                LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.defaultValue))
                    .foregroundStyle(.gray)
            }
        }
    }
}
```

**How to fix it:** Extract the branching logic into a separate function annotated with [`ChartContentBuilder`](https://developer.apple.com/documentation/Charts/ChartContentBuilder):

```swift
import SwiftUI
import Charts

struct MetricChartView: View {
    var selectedMetric: String
    var dataPoints: [DataPoint]

    var body: some View {
        Chart(dataPoints, id: \.index) { dataPoint in
            marks(for: dataPoint)
        }
    }

    @ChartContentBuilder
    private func marks(for dataPoint: DataPoint) -> some ChartContent {
        if selectedMetric == "Rate" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rate))
                .foregroundStyle(.blue)
        } else if selectedMetric == "Signal" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.signal))
                .foregroundStyle(.green)
        } else if selectedMetric == "Noise" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.noise))
                .foregroundStyle(.red)
        } else if selectedMetric == "Errors" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.errors))
                .foregroundStyle(.orange)
        } else if selectedMetric == "Throughput" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.throughput))
                .foregroundStyle(.purple)
        } else if selectedMetric == "TX Rate" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.txRate))
                .foregroundStyle(.cyan)
        } else if selectedMetric == "RX Rate" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rxRate))
                .foregroundStyle(.mint)
        } else if selectedMetric == "TX Frames" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.txFrames))
                .foregroundStyle(.indigo)
        } else if selectedMetric == "RX Frames" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rxFrames))
                .foregroundStyle(.brown)
        } else if selectedMetric == "Channel" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.channel))
                .foregroundStyle(.teal)
        } else if selectedMetric == "Bandwidth" {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.bandwidth))
                .foregroundStyle(.pink)
        } else {
            LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.defaultValue))
                .foregroundStyle(.gray)
        }
    }
}
```

**Why this occurs:** Supporting back-deployment of `@ContentBuilder` in Swift Charts requires a compatibility overload of `buildEither` that returns a Charts-specific `BuilderConditional` type. The presence of this additional overload increases the size of the candidate set the compiler must consider when resolving branching expressions inside chart builders. As the number of branches grows, the candidate set grows superlinearly, and beyond a certain point the expression exceeds the compiler’s complexity budget. Projects whose minimum deployment target is iOS 27, iPadOS 27, macOS 27, or visionOS 27 are unaffected because the compatibility overload is not compiled in. Extracting the branches into a dedicated `@ChartContentBuilder` function isolates the type-checking work and keeps each expression within budget. In aggregate, this trade-off improves type-checking performance for chart content outside this specific case, and for all SwiftUI content in projects that import Swift Charts.

#### Diagnostic Reference

To locate the section that addresses a specific build error, match the diagnostic text to the entry below.

| Type | Error | Learn More |
| --- | --- | --- |
| `@State` | `'self' used in property access '_x' before 'super.init' call` | [`Initialize stored properties before assigning to @State in init`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Initialize-stored-properties-before-assigning-to-State-in-init.md) |
| `@State` | `variable 'self.x' used before being initialized` | [`Initialize stored properties before assigning to @State in init`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Initialize-stored-properties-before-assigning-to-State-in-init.md) |
| `@State` | `invalid redeclaration of synthesized property '_x'` | [`Avoid composing additional property wrappers with @State`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Avoid-composing-additional-property-wrappers-with-State.md) |
| `@State` | Memberwise initializer not callable from extension | [`Define memberwise initializers explicitly when a view has private @State`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Define-memberwise-initializers-explicitly-when-a-view-has-private-State.md) |
| `@ContentBuilder` | `ambiguous use of 'opacity'` or `ambiguous use of 'blendMode'` in `background` or `overlay` | [`Use the closure-based forms of background and overlay for ShapeStyle expressions`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Use-the-closure-based-forms-of-background-and-overlay-for-ShapeStyle-expressions.md) |
| `@ContentBuilder` | `ambiguous use of '<member>'` for a SwiftUI member when another module declares a colliding type | [`Disambiguate types and members that collide across modules`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Disambiguate-types-and-members-that-collide-across-modules.md) |
| `@ContentBuilder` | `cannot convert value of type ... TupleContent ... to expected argument type ... TupleView ...` | [`Update generic constraints that reference TupleView`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Update-generic-constraints-that-reference-TupleView.md) |
| `@ContentBuilder` | `return type of property 'body' requires that 'EmptyMapContent' conform to 'View'` | [`Provide an explicit empty content value in nested builders when MapKit is in scope`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Provide-an-explicit-empty-content-value-in-nested-builders-when-MapKit-is-in-scope.md) |
| `@ContentBuilder` | `the compiler is unable to type-check this expression in reasonable time` inside `Chart` | [`Extract deeply branching content from Chart closures when back-deploying`](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder#Extract-deeply-branching-content-from-Chart-closures-when-back-deploying.md) |

#### Revision History

- **2026-06-08** First published.

## See Also

- [TN3213: Moving from Multipeer Connectivity to Network framework](tn3213-moving-from-multipeer-connectivity-to-network-framework.md)
  Learn how to migrate your Multipeer Connectivity app to Network framework.
- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.
- [TN3208: Preparing your app’s launch screen to meet App Store requirements](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md)
  Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.
- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder)*