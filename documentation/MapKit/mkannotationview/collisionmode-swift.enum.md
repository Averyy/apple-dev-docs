# MKAnnotationView.CollisionMode

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MKAnnotationViewCollisionMode : NSInteger;
```

## Topics

### Enumeration Cases
- [MKAnnotationView.CollisionMode.rectangle](./collisionmode-swift.enum/rectangle.md)
  A constant that indicates that the annotation view uses the full collision frame rectangle for detecting collisions.
- [MKAnnotationView.CollisionMode.circle](./collisionmode-swift.enum/circle.md)
  A constant that indicates that the annotation view uses an inscribed circle in the collision frame rectangle to determine collisions.
- [MKAnnotationView.CollisionMode.none](./collisionmode-swift.enum/none.md)
  A constant indicating that collisions can’t occur.
- [MKAnnotationView.CollisionMode.rectangle](./collisionmode-swift.enum/rectangle.md)
  A constant that indicates that the annotation view uses the full collision frame rectangle for detecting collisions.
- [MKAnnotationView.CollisionMode.circle](./collisionmode-swift.enum/circle.md)
  A constant that indicates that the annotation view uses an inscribed circle in the collision frame rectangle to determine collisions.
- [MKAnnotationView.CollisionMode.none](./collisionmode-swift.enum/none.md)
  A constant indicating that collisions can’t occur.
### Initializers
- [init?(rawValue: Int)](./collisionmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing collisions between annotation views
- [var collisionMode: MKAnnotationView.CollisionMode](./collisionmode-swift.property.md)
  The collision mode to use when interpreting the collision frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/collisionmode-swift.enum)*