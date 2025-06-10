# boundsMargin

**Framework**: RealityKit  
**Kind**: property

A margin applied to an entity’s bounding box that determines object visibility.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var boundsMargin: Float { get set }
```

## Mentions

- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)

#### Discussion

When determining which entities are currently visible, RealityKit tests each entity’s bounding box to see if it overlaps with the camera’s field of view (also known as the camera’s ). For efficiency, entities with a bounding box that don’t overlap the camera’s frustum aren’t rendered. Use this property to prevent RealityKit from incorrectly culling entities that use a [`CustomMaterial`](custommaterial.md) with a geometry modifier that moves vertices outside of the entity’s bounding box.

RealityKit adds the value of `boundsMargin` to the bounding box before determining which entities are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelcomponent/boundsmargin)*