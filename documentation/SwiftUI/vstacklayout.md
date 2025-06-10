# VStackLayout

**Framework**: SwiftUI  
**Kind**: struct

A vertical container that you can use in conditional layouts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@frozen
struct VStackLayout
```

#### Overview

This layout container behaves like a [`VStack`](vstack.md), but conforms to the [`Layout`](layout.md) protocol so you can use it in the conditional layouts that you construct with [`AnyLayout`](anylayout.md). If you don’t need a conditional layout, use [`VStack`](vstack.md) instead.

## Topics

### Creating a vertical stack
- [init(alignment: HorizontalAlignment, spacing: CGFloat?)](vstacklayout/init(alignment:spacing:).md)
  Creates a vertical stack with the specified spacing and horizontal alignment.
### Getting the stack’s properties
- [var alignment: HorizontalAlignment](vstacklayout/alignment.md)
  The horizontal alignment of subviews.
- [var spacing: CGFloat?](vstacklayout/spacing.md)
  The distance between adjacent subviews.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Layout](layout.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnyLayout](anylayout.md)
  A type-erased instance of the layout protocol.
- [struct HStackLayout](hstacklayout.md)
  A horizontal container that you can use in conditional layouts.
- [struct ZStackLayout](zstacklayout.md)
  An overlaying container that you can use in conditional layouts.
- [struct GridLayout](gridlayout.md)
  A grid that you can use in conditional layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vstacklayout)*