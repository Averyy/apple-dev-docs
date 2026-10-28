# externalForces

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The external forces applied to the particles in the body (in Newtons).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>
```

## Discussion

By default, the external forces are set to the zero vector.

## See Also

### Applying external forces
- [ClothBodyComponent.ExternalForce](./externalforce.md)
  An external force applied to a single particle, in Newtons.
- [var inflationConstraint: ClothBodyComponent.InflationConstraint?](./inflationconstraint-swift.property.md)
  An optional inflation constraint for representing inflatable bodies (must be watertight).
- [ClothBodyComponent.InflationConstraint](./inflationconstraint-swift.struct.md)
  Configuration for an inflatable cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/externalforces)*