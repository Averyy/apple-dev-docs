# enableCollisions(towards:)

**Framework**: RealityKit  
**Kind**: method

Enables one-way collisions towards the selected groups.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func enableCollisions(towards groups: ClothCollisionGroupSet)
```

#### Discussion

This adds the selected groups to the collider’s mask, causing body particles in those groups to be pushed away by this collider.

## Parameters

- `groups`: The collision groups to add to the collider’s mask.

## See Also

- [var isCollisionResponseEnabled: Bool](clothcollidercomponent/iscollisionresponseenabled.md)
  Indicates whether this collider pushes away intersecting cloth body particles.
- [func disableCollisions(towards: ClothCollisionGroupSet)](clothcollidercomponent/disablecollisions(towards:).md)
  Disables one-way collisions towards the selected groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent/enablecollisions(towards:))*