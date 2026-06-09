# collisions

**Framework**: RealityKit  
**Kind**: property

The collisions with cloth bodies that took place.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var collisions: Span<ClothColliderEvents.NewBodyCollisions.Collision> { get }
```

#### Discussion

The lifetime of this span is tied to the owning event, and thus cannot escape it. This data is only available during the subscription callback in which the owning event is provided. If you store the event and attempt to access this data after the subscription callback, then you will get an empty span instead.

## See Also

- [func withCollisions<Result>((Span<ClothColliderEvents.NewBodyCollisions.Collision>) -> Result) -> Result](clothcolliderevents/newbodycollisions/withcollisions(_:).md)
  Provides access to the collisions with cloth bodies that took place.
- [ClothColliderEvents.NewBodyCollisions.Collision](clothcolliderevents/newbodycollisions/collision.md)
  A collision with a cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions/collisions)*