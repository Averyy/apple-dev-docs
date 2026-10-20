# mass

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Mass of the body as a whole, in Kg.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var mass: Float { get set }
```

#### Discussion

The mass specified here is distributed equally among the particles forming the body for simulation purposes. A higher mass will resist acceleration changes from forces such as wind and external forces.

Must be positive. The default value is `1.0`.

## See Also

### Controlling cloth motion
- [var motionTypes: PerClothVertexData<ClothBodyComponent.ParticleMotionType>](./motiontypes.md)
  Motion types for each particle in the body.
- [ClothBodyComponent.ParticleMotionType](./particlemotiontype.md)
  Defines whether a particle is moved by the simulation or by the entity transform.
- [static func resetDeformation(entity: Entity)](./resetdeformation%28entity%29.md)
  Resets the deformation of the cloth body to its initial pose and motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/mass)*