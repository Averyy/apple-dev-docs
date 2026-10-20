# ClothBodyComponent.ParticleMotionType

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines whether a particle is moved by the simulation or by the entity transform.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ParticleMotionType
```

## Topics

### Type Properties
- [static var dynamic: ClothBodyComponent.ParticleMotionType](./particlemotiontype/dynamic.md)
  Dynamic particles are moved exclusively by the simulation, and ignore changes to the entity transform.
- [static var kinematic: ClothBodyComponent.ParticleMotionType](./particlemotiontype/kinematic.md)
  Kinematic particles are moved with the entity transform, and cannot be moved in any way by the simulation.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling cloth motion
- [var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>](./motiontypes.md)
  Motion types for each particle in the body.
- [var mass: Float](./mass.md)
  Mass of the body as a whole, in Kg.
- [static func resetDeformation(entity: Entity)](./resetdeformation%28entity%29.md)
  Resets the deformation of the cloth body to its initial pose and motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/particlemotiontype)*