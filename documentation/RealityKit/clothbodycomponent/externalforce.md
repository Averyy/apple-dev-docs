# ClothBodyComponent.ExternalForce

**Framework**: RealityKit  
**Kind**: struct

An external force applied to a single particle, in Newtons.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ExternalForce
```

## Topics

### Accessing the force vector
- [var vector: SIMD3<Float>](clothbodycomponent/externalforce/vector.md)
  The force vector applied to the particle, in Newtons.
### Initializers
- [init()](clothbodycomponent/externalforce/init.md)
  Creates an external force with zero magnitude.
- [init(SIMD3<Float>)](clothbodycomponent/externalforce/init(_:).md)
  Creates an external force with the given force vector.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>](clothbodycomponent/externalforces.md)
  The external forces applied to the particles in the body (in Newtons).
- [var inflationConstraint: ClothBodyComponent.InflationConstraint?](clothbodycomponent/inflationconstraint-swift.property.md)
  An optional inflation constraint for representing inflatable bodies (must be watertight).
- [ClothBodyComponent.InflationConstraint](clothbodycomponent/inflationconstraint-swift.struct.md)
  Configuration for an inflatable cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/externalforce)*