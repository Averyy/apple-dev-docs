# motionTypes

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Motion types for each particle in the body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>
```

## Discussion

By default, the motion types are set to `.dynamic`.

## See Also

### Controlling cloth motion
- [ClothBodyComponent.ParticleMotionType](./particlemotiontype.md)
  Defines whether a particle is moved by the simulation or by the entity transform.
- [var mass: Float](./mass.md)
  Mass of the body as a whole, in Kg.
- [static func resetDeformation(entity: Entity)](./resetdeformation%28entity%29.md)
  Resets the deformation of the cloth body to its initial pose and motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/motiontypes)*