# Viewpoint

**Framework**: Compute Graph  
**Kind**: struct

Camera viewpoint parameters in 3D space.

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
struct Viewpoint
```

#### Overview

This structure represents a camera or observer’s position and viewing direction, with optional availability flags for each component. This allows partial viewpoint information to be represented when only position or direction is known.

## Topics

### Initializers
- [init()](viewpoint-swift.struct/init.md)
- [init(position: simd_float3, direction: simd_float3, has_position: Bool, has_direction: Bool)](viewpoint-swift.struct/init(position:direction:has_position:has_direction:).md)
### Instance Properties
- [var direction: simd_float3](viewpoint-swift.struct/direction.md)
  The normalized direction vector indicating where the camera is looking, in the simulation’s coordinate system
- [var has_direction: Bool](viewpoint-swift.struct/has_direction.md)
  Indicates whether a valid direction is available.
- [var has_position: Bool](viewpoint-swift.struct/has_position.md)
  Indicates whether a valid position is available.
- [var position: simd_float3](viewpoint-swift.struct/position.md)
  The 3D position of the camera or viewpoint, in the simulation’s coordinate system.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/viewpoint-swift.struct)*