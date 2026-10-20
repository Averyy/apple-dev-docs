# ClothBodyComponent.ExternalForce

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An external force applied to a single particle, in Newtons.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ExternalForce
```

## Topics

### Accessing the force vector
- [var vector: SIMD3<Float>](./externalforce/vector.md)
  The force vector applied to the particle, in Newtons.
### Initializers
- [init()](./externalforce/init%28%29.md)
  Creates an external force with zero magnitude.
- [init(SIMD3<Float>)](./externalforce/init%28_%29.md)
  Creates an external force with the given force vector.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying external forces
- [var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>](./externalforces.md)
  The external forces applied to the particles in the body (in Newtons).
- [var inflationConstraint: ClothBodyComponent.InflationConstraint?](./inflationconstraint-swift.property.md)
  An optional inflation constraint for representing inflatable bodies (must be watertight).
- [ClothBodyComponent.InflationConstraint](./inflationconstraint-swift.struct.md)
  Configuration for an inflatable cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/externalforce)*