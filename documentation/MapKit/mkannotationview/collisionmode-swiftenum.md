# MKAnnotationView.CollisionMode

**Framework**: MapKit  
**Kind**: enum

Constants that indicates how to interpret the collision frame rectangle of an annotation view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum CollisionMode
```

## Topics

### Enumeration Cases
- [MKAnnotationView.CollisionMode.rectangle](mkannotationview/collisionmode-swift.enum/rectangle.md)
  A constant that indicates that the annotation view uses the full collision frame rectangle for detecting collisions.
- [MKAnnotationView.CollisionMode.circle](mkannotationview/collisionmode-swift.enum/circle.md)
  A constant that indicates that the annotation view uses an inscribed circle in the collision frame rectangle to determine collisions.
- [MKAnnotationView.CollisionMode.none](mkannotationview/collisionmode-swift.enum/none.md)
  A constant indicating that collisions can’t occur.
- [MKAnnotationView.CollisionMode.rectangle](mkannotationview/collisionmode-swift.enum/rectangle.md)
  A constant that indicates that the annotation view uses the full collision frame rectangle for detecting collisions.
- [MKAnnotationView.CollisionMode.circle](mkannotationview/collisionmode-swift.enum/circle.md)
  A constant that indicates that the annotation view uses an inscribed circle in the collision frame rectangle to determine collisions.
- [MKAnnotationView.CollisionMode.none](mkannotationview/collisionmode-swift.enum/none.md)
  A constant indicating that collisions can’t occur.
### Initializers
- [init?(rawValue: Int)](mkannotationview/collisionmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var collisionMode: MKAnnotationView.CollisionMode](mkannotationview/collisionmode-swift.property.md)
  The collision mode to use when interpreting the collision frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/collisionmode-swift.enum)*