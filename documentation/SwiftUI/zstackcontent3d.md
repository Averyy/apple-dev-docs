# ZStackContent3D

**Framework**: SwiftUI  
**Kind**: struct

A type that adds spacing to a [`ZStack`](zstack.md).

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@frozen
struct ZStackContent3D<Content> where Content : View
```

#### Overview

You don’t create this type directly. SwiftUI creates it for you when you use the `ZStack(alignment:spacing:content)` initializer.

## Topics

### Initializers
- [init(spacing: CGFloat?, content: Content)](zstackcontent3d/init(spacing:content:).md)
### Instance Properties
- [var content: Content](zstackcontent3d/content.md)
- [var spacing: CGFloat?](zstackcontent3d/spacing.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [View](view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zstackcontent3d)*