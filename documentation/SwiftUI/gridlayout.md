# GridLayout

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A grid that you can use in conditional layouts.

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
nonisolated struct GridLayout
```

#### Overview

This layout container behaves like a [`Grid`](./grid.md), but conforms to the [`Layout`](./layout.md) protocol so you can use it in the conditional layouts that you construct with [`AnyLayout`](./anylayout.md). If you don’t need a conditional layout, use [`Grid`](./grid.md) instead.

## Topics

### Creating a grid
- [init(alignment: Alignment, horizontalSpacing: CGFloat?, verticalSpacing: CGFloat?)](./gridlayout/init%28alignment,horizontalspacing,verticalspacing%29.md)
  Creates a grid with the specified spacing and alignment.
### Getting the grid’s properties
- [var alignment: Alignment](./gridlayout/alignment.md)
  The alignment of subviews.
- [var horizontalSpacing: CGFloat?](./gridlayout/horizontalspacing.md)
  The horizontal distance between adjacent subviews.
- [var verticalSpacing: CGFloat?](./gridlayout/verticalspacing.md)
  The vertical distance between adjacent subviews.
### Type Aliases
- [GridLayout.Body](./gridlayout/body.md)
### Default Implementations
- [Layout Implementations](./gridlayout/layout-implementations.md)

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Layout](./layout.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Transitioning between layout types
- [struct AnyLayout](./anylayout.md)
  A type-erased instance of the layout protocol.
- [struct HStackLayout](./hstacklayout.md)
  A horizontal container that you can use in conditional layouts.
- [struct VStackLayout](./vstacklayout.md)
  A vertical container that you can use in conditional layouts.
- [struct ZStackLayout](./zstacklayout.md)
  An overlaying container that you can use in conditional layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gridlayout)*