# MouseParams

**Framework**: Compute Graph  
**Kind**: struct

Parameters describing mouse interaction in 3D space.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- Reality Composer Pro ?+

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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/mouseparams)*