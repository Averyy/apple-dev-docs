# resetDeformation(entity:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Resets the deformation of the cloth body to its initial pose and motion.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func resetDeformation(entity: Entity)
```

## Parameters

- `entity`: The entity whose cloth body should be reset.

## See Also

### Controlling cloth motion
- [var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>](./motiontypes.md)
  Motion types for each particle in the body.
- [ClothBodyComponent.ParticleMotionType](./particlemotiontype.md)
  Defines whether a particle is moved by the simulation or by the entity transform.
- [var mass: Float](./mass.md)
  Mass of the body as a whole, in Kg.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/resetdeformation(entity:))*