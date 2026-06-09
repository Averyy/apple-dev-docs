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

- [Declaring a custom view](declaring-a-custom-view.md)
- [Populating SwiftUI menus with adaptive controls](populating-swiftui-menus-with-adaptive-controls.md)

#### Overview

When you build your project in Xcode 26 and earlier, use [`ViewBuilder`](viewbuilder.md) as a parameter attribute for view-producing closure parameters, allowing those closures to provide multiple child views. For example, the following `contextMenu` function accepts a closure that produces one or more views via the view builder.

```swift
func contextMenu<MenuItems: View>(
    @ViewBuilder menuItems: () -> MenuItems
) -> some View
```

Clients of this function can use multiple-statement closures to provide several child views, as the following example shows:

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

When you build in Xcode 27 and later for any version of SwiftUI, the system constructs type-agnostic content from `ViewBuilder` closures, and doesn’t restrict the types you use in closures to conform to [`View`](view.md). Mark closures with the type alias [`ContentBuilder`](contentbuilder.md) instead to indicate where your code expects this behavior. For more information, see [`ContentBuilder`](contentbuilder.md).

## Topics

### Building content
- [static buildBlock()](viewbuilder/buildblock.md)
  Builds an empty content from a block containing no statements.
- [static buildBlock(_:)](viewbuilder/buildblock(_:).md)
  Passes a single piece of content written as a child view through unmodified.
### Conditionally building content
- [static buildEither(first:)](viewbuilder/buildeither(first:).md)
  Builds a partial result from a condition that’s true.
- [static buildEither(second:)](viewbuilder/buildeither(second:).md)
  Builds a partial result from a condition that’s false.
- [static buildIf(_:)](viewbuilder/buildif(_:).md)
  Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
- [static buildLimitedAvailability(_:)](viewbuilder/buildlimitedavailability(_:).md)

## See Also

- [Declaring a custom view](declaring-a-custom-view.md)
  Define views and assemble them into a view hierarchy.
- [Wishlist: Planning travel in a SwiftUI app](wishlist-planning-travel-in-a-swiftui-app.md)
  Build a travel planning app that organizes trips into collections and tracks activity completion.
- [protocol View](view.md)
  A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
- [typealias ContentBuilder](contentbuilder.md)
  A custom parameter attribute that constructs views and other content types from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder)*