# enableCollisions(towards:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Enables one-way collisions towards the selected groups.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func enableCollisions(towards groups: ClothCollisionGroupSet)
```

#### Discussion

This adds the selected groups to the collider’s mask, causing body particles in those groups to be pushed away by this collider.

## Parameters

- `groups`: The collision groups to add to the collider’s mask.

## See Also

### Managing collision response
- [var isCollisionResponseEnabled: Bool](./iscollisionresponseenabled.md)
  Indicates whether this collider pushes away intersecting cloth body particles.
- [func disableCollisions(towards: ClothCollisionGroupSet)](./disablecollisions%28towards%29.md)
  Disables one-way collisions towards the selected groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent/enablecollisions(towards:))*