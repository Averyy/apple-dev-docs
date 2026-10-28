# disableCollisions(towards:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Disables one-way collisions towards the selected groups.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func disableCollisions(towards groups: ClothCollisionGroupSet)
```

## Discussion

This removes the selected groups from the collider’s mask, so that body particles in those groups will no longer be pushed away by this collider.

## Parameters

- `groups`: The collision groups to remove from the collider’s mask.

## See Also

### Managing collision response
- [var isCollisionResponseEnabled: Bool](./iscollisionresponseenabled.md)
  Indicates whether this collider pushes away intersecting cloth body particles.
- [func enableCollisions(towards: ClothCollisionGroupSet)](./enablecollisions%28towards%29.md)
  Enables one-way collisions towards the selected groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent/disablecollisions(towards:))*