# ElementSpawnParameters

**Framework**: Compute Graph  
**Kind**: struct

Parameters used to configure the initial state of a particle when it’s spawned in the simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
struct ElementSpawnParameters
```

#### Overview

The values specified become initial values in the Initialization stage, which can read or overwrite the values.

#### Usage

```swift
let params = ElementSpawnParameters(
    position: SIMD3<Float>(0, 1, 0),
    velocity: SIMD3<Float>(0, -1, 0),
    size: SIMD2<Float>(0.02, 0.02),
    color: SIMD4<Float>(1, 0.5, 0, 1),
    lifetime: 2.0
)
```

## Topics

### Initializers
- [init(position: SIMD3<Float>, velocity: SIMD3<Float>, size: SIMD2<Float>, color: SIMD4<Float>, lifetime: Float)](elementspawnparameters/init(position:velocity:size:color:lifetime:).md)
  Creates a new set of particle spawn parameters.
### Instance Properties
- [var color: SIMD4<Float>](elementspawnparameters/color.md)
  The initial color and alpha (transparency) of the particle.
- [var lifetime: Float](elementspawnparameters/lifetime.md)
  The initial lifetime of the particle in seconds.
- [var position: SIMD3<Float>](elementspawnparameters/position.md)
  The initial 3D position of the particle in world space coordinates.
- [var size: SIMD2<Float>](elementspawnparameters/size.md)
  The initial size of the particle as a 2D vector representing width and height.
- [var velocity: SIMD3<Float>](elementspawnparameters/velocity.md)
  The initial velocity vector of the particle in world space units per second.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ElementGrouping](elementgrouping.md)
  An enumeration of how elements are grouped.
- [enum Sorting](sorting.md)
  An enumeration of sorting modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters)*