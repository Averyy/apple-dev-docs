# withCollisions(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the collisions with cloth bodies that took place.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withCollisions<Result>(_ callback: (Span<ClothColliderEvents.NewBodyCollisions.Collision>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

This span is only available during the subscription callback of this event. The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a span over the collisions.

## See Also

- [var collisions: Span<ClothColliderEvents.NewBodyCollisions.Collision>](clothcolliderevents/newbodycollisions/collisions.md)
  The collisions with cloth bodies that took place.
- [ClothColliderEvents.NewBodyCollisions.Collision](clothcolliderevents/newbodycollisions/collision.md)
  A collision with a cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions/withcollisions(_:))*