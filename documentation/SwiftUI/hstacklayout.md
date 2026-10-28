# HStackLayout

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A horizontal container that you can use in conditional layouts.

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
struct HStackLayout
```

## Overview

This layout container behaves like an [`HStack`](./hstack.md), but conforms to the [`Layout`](./layout.md) protocol so you can use it in the conditional layouts that you construct with [`AnyLayout`](./anylayout.md). If you don’t need a conditional layout, use [`HStack`](./hstack.md) instead.

## Topics

### Creating a horizontal stack
- [init(alignment: VerticalAlignment, spacing: CGFloat?)](./hstacklayout/init%28alignment,spacing%29.md)
  Creates a horizontal stack with the specified spacing and vertical alignment.
### Getting the stack’s properties
- [var alignment: VerticalAlignment](./hstacklayout/alignment.md)
  The vertical alignment of subviews.
- [var spacing: CGFloat?](./hstacklayout/spacing.md)
  The distance between adjacent subviews.

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Layout](./layout.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Transitioning between layout types
- [struct AnyLayout](./anylayout.md)
  A type-erased instance of the layout protocol.
- [struct VStackLayout](./vstacklayout.md)
  A vertical container that you can use in conditional layouts.
- [struct ZStackLayout](./zstacklayout.md)
  An overlaying container that you can use in conditional layouts.
- [struct GridLayout](./gridlayout.md)
  A grid that you can use in conditional layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hstacklayout)*