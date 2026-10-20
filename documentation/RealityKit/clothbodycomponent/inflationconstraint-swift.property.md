# inflationConstraint

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An optional inflation constraint for representing inflatable bodies (must be watertight).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var inflationConstraint: ClothBodyComponent.InflationConstraint? { get set }
```

#### Discussion

When non-nil, the body will try to maintain the specified target volume with the given stiffness. The mesh must be watertight for this inflation constraint to have any effect.

Setting this to `nil` disables the inflation constraint (equivalent to a stiffness of zero).

## See Also

### Applying external forces
- [var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>](./externalforces.md)
  The external forces applied to the particles in the body (in Newtons).
- [ClothBodyComponent.ExternalForce](./externalforce.md)
  An external force applied to a single particle, in Newtons.
- [ClothBodyComponent.InflationConstraint](./inflationconstraint-swift.struct.md)
  Configuration for an inflatable cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.property)*