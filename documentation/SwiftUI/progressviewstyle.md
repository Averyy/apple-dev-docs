# ProgressViewStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that applies standard interaction behavior to all progress views within a view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol ProgressViewStyle
```

#### Overview

To configure the current progress view style for a view hierarchy, use the [`progressViewStyle(_:)`](view/progressviewstyle(_:).md) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting built-in progress view styles
- [static var automatic: DefaultProgressViewStyle](progressviewstyle/automatic.md)
  The default progress view style in the current context of the view being styled.
- [static var circular: CircularProgressViewStyle](progressviewstyle/circular.md)
  The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.
- [static var linear: LinearProgressViewStyle](progressviewstyle/linear.md)
  A progress view that visually indicates its progress using a horizontal bar.
### Creating custom progress view styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](progressviewstyle/makebody(configuration:).md)
  Creates a view representing the body of a progress view.
- [ProgressViewStyle.Configuration](progressviewstyle/configuration.md)
  A type alias for the properties of a progress view instance.
- [associatedtype Body : View](progressviewstyle/body.md)
  A view representing the body of a progress view.
### Supporting types
- [struct DefaultProgressViewStyle](defaultprogressviewstyle.md)
  The default progress view style in the current context of the view being styled.
- [struct CircularProgressViewStyle](circularprogressviewstyle.md)
  A progress view that uses a circular gauge to indicate the partial completion of an activity.
- [struct LinearProgressViewStyle](linearprogressviewstyle.md)
  A progress view that visually indicates its progress using a horizontal bar.

## Relationships

### Conforming Types
- [CircularProgressViewStyle](circularprogressviewstyle.md)
- [DefaultProgressViewStyle](defaultprogressviewstyle.md)
- [LinearProgressViewStyle](linearprogressviewstyle.md)

## See Also

- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [protocol GaugeStyle](gaugestyle.md)
  Defines the implementation of all gauge instances within a view hierarchy.
- [struct GaugeStyleConfiguration](gaugestyleconfiguration.md)
  The properties of a gauge instance.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [struct ProgressViewStyleConfiguration](progressviewstyleconfiguration.md)
  The properties of a progress view instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressviewstyle)*