# Chart3D

**Framework**: Swift Charts  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct Chart3D<Content> where Content : Chart3DContent
```

## Topics

### Initializers
- [init<Data, C>(Data, content: (Data.Element) -> C)](chart3d/init(_:content:).md)
  Creates a 3D chart composed of a series of identifiable marks.
- [init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> C)](chart3d/init(_:id:content:).md)
  Creates a 3D chart composed of a series of marks.
- [init(content: () -> Content)](chart3d/init(content:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3d)*