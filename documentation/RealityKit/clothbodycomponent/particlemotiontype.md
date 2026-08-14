# ClothBodyComponent.ParticleMotionType

**Framework**: RealityKit  
**Kind**: struct

Defines whether a particle is moved by the simulation or by the entity transform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ParticleMotionType
```

## Topics

### Type Properties
- [static var dynamic: ClothBodyComponent.ParticleMotionType](clothbodycomponent/particlemotiontype/dynamic.md)
  Dynamic particles are moved exclusively by the simulation, and ignore changes to the entity transform.
- [static var kinematic: ClothBodyComponent.ParticleMotionType](clothbodycomponent/particlemotiontype/kinematic.md)
  Kinematic particles are moved with the entity transform, and cannot be moved in any way by the simulation.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>](clothbodycomponent/motiontypes.md)
  Motion types for each particle in the body.
- [var mass: Float](clothbodycomponent/mass.md)
  Mass of the body as a whole, in Kg.
- [static func resetDeformation(entity: Entity)](clothbodycomponent/resetdeformation(entity:).md)
  Resets the deformation of the cloth body to its initial pose and motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/particlemotiontype)*