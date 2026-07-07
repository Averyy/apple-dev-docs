# motionTypes

**Framework**: RealityKit  
**Kind**: property

Motion types for each particle in the body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>
```

#### Discussion

By default, the motion types are set to `.dynamic`.

## See Also

- [ClothBodyComponent.ParticleMotionType](clothbodycomponent/particlemotiontype.md)
  Defines whether a particle is moved by the simulation or by the entity transform.
- [var mass: Float](clothbodycomponent/mass.md)
  Mass of the body as a whole, in Kg.
- [static func resetDeformation(entity: Entity)](clothbodycomponent/resetdeformation(entity:).md)
  Resets the deformation of the cloth body to its initial pose and motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/motiontypes)*