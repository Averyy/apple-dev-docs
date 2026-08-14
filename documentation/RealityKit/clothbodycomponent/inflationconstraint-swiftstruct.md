# ClothBodyComponent.InflationConstraint

**Framework**: RealityKit  
**Kind**: struct

Configuration for an inflatable cloth body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct InflationConstraint
```

## Topics

### Creating an inflation constraint
- [init(targetVolume: Float, stiffness: Float)](clothbodycomponent/inflationconstraint-swift.struct/init(targetvolume:stiffness:).md)
  Creates an inflation configuration.
- [init(stiffness: Float)](clothbodycomponent/inflationconstraint-swift.struct/init(stiffness:).md)
  Creates an inflation configuration that defaults to the mesh volume.
### Configuring inflation
- [var targetVolume: Float?](clothbodycomponent/inflationconstraint-swift.struct/targetvolume.md)
  The target volume (in ㎥) that the body tries to match.
- [var stiffness: Float](clothbodycomponent/inflationconstraint-swift.struct/stiffness.md)
  The resistance of the body’s volume to diverge from `targetVolume`.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var externalForces: PerClothVertexData<ClothBodyComponent.ExternalForce>](clothbodycomponent/externalforces.md)
  The external forces applied to the particles in the body (in Newtons).
- [ClothBodyComponent.ExternalForce](clothbodycomponent/externalforce.md)
  An external force applied to a single particle, in Newtons.
- [var inflationConstraint: ClothBodyComponent.InflationConstraint?](clothbodycomponent/inflationconstraint-swift.property.md)
  An optional inflation constraint for representing inflatable bodies (must be watertight).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct)*