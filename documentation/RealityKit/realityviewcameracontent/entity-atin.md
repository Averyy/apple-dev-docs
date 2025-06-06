# entity(at:in:)

**Framework**: RealityKit  
**Kind**: method

Finds the first entity hit when projecting a ray from a starting point.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func entity(at point: CGPoint, in space: some CoordinateSpaceProtocol) -> Entity?
```

#### Return Value

The entity at `point`. Returns `nil` if no entity was found.

#### Discussion

> ❗ **Important**: RealityKit performs hit tests (ray-casts) against collision shapes. Entities without a valid [`CollisionComponent`](collisioncomponent.md) are ignored by hit tests.

RealityKit performs hit tests (ray-casts) against collision shapes. Entities without a valid [`CollisionComponent`](collisioncomponent.md) are ignored by hit tests.

## Parameters

- `point`: A point in the provided coordinate space.
- `space`: The 2D coordinate space in which to interpret the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/entity(at:in:))*