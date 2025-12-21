# HStack

**Framework**: SwiftUI  
**Kind**: struct

A view that arranges its subviews in a horizontal line.

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
struct HStack<Content> where Content : View
```

## Mentions

- [Building layouts with stack views](building-layouts-with-stack-views.md)
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Laying out a simple view](laying-out-a-simple-view.md)
- [Aligning views across stacks](aligning-views-across-stacks.md)
- [Aligning views within a stack](aligning-views-within-a-stack.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Overview

Unlike [`LazyHStack`](lazyhstack.md), which only renders the views when your app needs to display them onscreen, an `HStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `HStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple horizontal stack of five text views:

```swift
var body: some View {
    HStack(
        alignment: .top,
        spacing: 10
    ) {
        ForEach(
            1...5,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

![Five text views, named Item 1 through Item 5, arranged in a](https://docs-assets.developer.apple.com/published/4d9bc52c0fbde5252c797d82d913a50b/SwiftUI-HStack-simple%402x.png)

> **Note**: If you need a horizontal stack that conforms to the [`Layout`](layout.md) protocol, like when you want to create a conditional layout using [`AnyLayout`](anylayout.md), use [`HStackLayout`](hstacklayout.md) instead.

## Topics

### Creating a stack
- [init(alignment: VerticalAlignment, spacing: CGFloat?, content: () -> Content)](hstack/init(alignment:spacing:content:).md)
  Creates a horizontal stack with the given spacing and vertical alignment.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Building layouts with stack views](building-layouts-with-stack-views.md)
  Compose complex layouts from primitive container views.
- [struct VStack](vstack.md)
  A view that arranges its subviews in a vertical line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hstack)*