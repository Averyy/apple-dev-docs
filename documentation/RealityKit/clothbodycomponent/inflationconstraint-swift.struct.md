# ClothBodyComponent.InflationConstraint

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Configuration for an inflatable cloth body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct InflationConstraint
```

## Topics

### Creating an inflation constraint
- [init(targetVolume: Float, stiffness: Float)](./inflationconstraint-swift.struct/init%28targetvolume,stiffness%29.md)
  Creates an inflation configuration.
- [init(stiffness: Float)](./inflationconstraint-swift.struct/init%28stiffness%29.md)
  Creates an inflation configuration that defaults to the mesh volume.
### Configuring inflation
- [var targetVolume: Float?](./inflationconstraint-swift.struct/targetvolume.md)
  The target volume (in ㎥) that the body tries to match.
- [var stiffness: Float](./inflationconstraint-swift.struct/stiffness.md)
  The resistance of the body’s volume to diverge from `targetVolume`.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying external forces
- [var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>](./externalforces.md)
  The external forces applied to the particles in the body (in Newtons).
- [ClothBodyComponent.ExternalForce](./externalforce.md)
  An external force applied to a single particle, in Newtons.
- [var inflationConstraint: ClothBodyComponent.InflationConstraint?](./inflationconstraint-swift.property.md)
  An optional inflation constraint for representing inflatable bodies (must be watertight).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct)*