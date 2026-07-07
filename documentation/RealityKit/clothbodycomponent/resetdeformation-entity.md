# resetDeformation(entity:)

**Framework**: RealityKit  
**Kind**: method

Resets the deformation of the cloth body to its initial pose and motion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func resetDeformation(entity: Entity)
```

## Parameters

- `entity`: The entity whose cloth body should be reset.

## See Also

- [var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>](clothbodycomponent/motiontypes.md)
  Motion types for each particle in the body.
- [ClothBodyComponent.ParticleMotionType](clothbodycomponent/particlemotiontype.md)
  Defines whether a particle is moved by the simulation or by the entity transform.
- [var mass: Float](clothbodycomponent/mass.md)
  Mass of the body as a whole, in Kg.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/resetdeformation(entity:))*