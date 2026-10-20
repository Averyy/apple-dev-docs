# ZStackContent3D

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type that adds spacing to a [`ZStack`](./zstack.md).

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@frozen
nonisolated struct ZStackContent3D<Content> where Content : View
```

#### Overview

You don’t create this type directly. SwiftUI creates it for you when you use the `ZStack(alignment:spacing:content)` initializer.

## Topics

### Initializers
- [init(spacing: CGFloat?, content: Content)](./zstackcontent3d/init%28spacing,content%29.md)
### Instance Properties
- [var content: Content](./zstackcontent3d/content.md)
- [var spacing: CGFloat?](./zstackcontent3d/spacing.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [View](./view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zstackcontent3d)*