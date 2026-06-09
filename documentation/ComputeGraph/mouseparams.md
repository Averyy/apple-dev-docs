# MouseParams

**Framework**: ComputeGraph  
**Kind**: struct

Parameters describing mouse interaction in 3D space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
struct MouseParams
```

#### Overview

This structure captures both the position and direction of a mouse cursor projected into 3D coordinates, commonly used for ray casting or spatial interactions.

## Topics

### Initializers
- [init()](mouseparams/init.md)
- [init(position: simd_float3, direction: simd_float3, has_value: Bool)](mouseparams/init(position:direction:has_value:).md)
### Instance Properties
- [var direction: simd_float3](mouseparams/direction.md)
  The normalized direction vector of the mouse ray, converted to the simulation’s coordinate system.
- [var has_value: Bool](mouseparams/has_value.md)
  Indicates whether valid mouse parameters are available.
- [var position: simd_float3](mouseparams/position.md)
  The 3D position of the mouse cursor in local space, converted to the simulation’s coordinate system.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum Topology](topology.md)
- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/mouseparams)*