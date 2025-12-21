# VStack

**Framework**: SwiftUI  
**Kind**: struct

A view that arranges its subviews in a vertical line.

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
@frozen
struct VStack<Content> where Content : View
```

## Mentions

- [Building layouts with stack views](building-layouts-with-stack-views.md)
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Adding a background to your view](adding-a-background-to-your-view.md)
- [Inspecting view layout](inspecting-view-layout.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Aligning views across stacks](aligning-views-across-stacks.md)
- [Aligning views within a stack](aligning-views-within-a-stack.md)
- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
- [Configuring views](configuring-views.md)
- [Declaring a custom view](declaring-a-custom-view.md)

#### Overview

Unlike [`LazyVStack`](lazyvstack.md), which only renders the views when your app needs to display them, a `VStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `VStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple vertical stack of 10 text views:

```swift
var body: some View {
    VStack(
        alignment: .leading,
        spacing: 10
    ) {
        ForEach(
            1...10,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

![Ten text views, named Item 1 through Item 10, arranged in a](https://docs-assets.developer.apple.com/published/93d31b000cb6f5419689a7b765474401/SwiftUI-VStack-simple%402x.png)

> **Note**: If you need a vertical stack that conforms to the [`Layout`](layout.md) protocol, like when you want to create a conditional layout using [`AnyLayout`](anylayout.md), use [`VStackLayout`](vstacklayout.md) instead.

## Topics

### Creating a stack
- [init(alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> Content)](vstack/init(alignment:spacing:content:).md)
  Creates an instance with the given spacing and horizontal alignment.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Building layouts with stack views](building-layouts-with-stack-views.md)
  Compose complex layouts from primitive container views.
- [struct HStack](hstack.md)
  A view that arranges its subviews in a horizontal line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vstack)*