# ViewBuilder

**Framework**: SwiftUI  
**Kind**: struct

A custom parameter attribute that constructs views from closures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@resultBuilder
struct ViewBuilder
```

## Mentions

- [Populating SwiftUI menus with adaptive controls](populating-swiftui-menus-with-adaptive-controls.md)
- [Declaring a custom view](declaring-a-custom-view.md)

#### Overview

You typically use [`ViewBuilder`](viewbuilder.md) as a parameter attribute for child view-producing closure parameters, allowing those closures to provide multiple child views. For example, the following `contextMenu` function accepts a closure that produces one or more views via the view builder.

```swift
func contextMenu<MenuItems: View>(
    @ViewBuilder menuItems: () -> MenuItems
) -> some View
```

Clients of this function can use multiple-statement closures to provide several child views, as shown in the following example:

```swift
myView.contextMenu {
    Text("Cut")
    Text("Copy")
    Text("Paste")
    if isSymbol {
        Text("Jump to Definition")
    }
}
```

## Topics

### Building content
- [static func buildBlock() -> EmptyView](viewbuilder/buildblock.md)
  Builds an empty view from a block containing no statements.
- [static buildBlock(_:)](viewbuilder/buildblock(_:).md)
  Passes a single view written as a child view through unmodified.
- [static func buildExpression<Content>(Content) -> Content](viewbuilder/buildexpression(_:).md)
  Builds an expression within the builder.
### Conditionally building content
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildIf<Content>(Content?) -> Content?](viewbuilder/buildif(_:).md)
  Produces an optional view for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [static func buildLimitedAvailability<Content>(Content) -> AnyView](viewbuilder/buildlimitedavailability(_:).md)
  Processes view content for a conditional compiler-control statement that performs an availability check.

## See Also

- [Declaring a custom view](declaring-a-custom-view.md)
  Define views and assemble them into a view hierarchy.
- [protocol View](view.md)
  A type that represents part of your app’s user interface and provides modifiers that you use to configure views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder)*