# Viewpoint

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Camera viewpoint parameters in 3D space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- Reality Composer Pro

## Declaration

```swift
struct Viewpoint
```

```c
struct Viewpoint;
```

#### Overview

This structure represents a camera or observer’s position and viewing direction, with optional availability flags for each component. This allows partial viewpoint information to be represented when only position or direction is known.

## Topics

### Initializers
- [init()](./viewpoint-swift.struct/init%28%29.md)
- [init(position: simd_float3, direction: simd_float3, has_position: Bool, has_direction: Bool)](./viewpoint-swift.struct/init%28position,direction,has_position,has_direction%29.md)
### Instance Properties
- [var direction: simd_float3](./viewpoint-swift.struct/direction.md)
  The normalized direction vector indicating where the camera is looking, in the simulation’s coordinate system
- [var has_direction: Bool](./viewpoint-swift.struct/has_direction.md)
  Indicates whether a valid direction is available.
- [var has_position: Bool](./viewpoint-swift.struct/has_position.md)
  Indicates whether a valid position is available.
- [var position: simd_float3](./viewpoint-swift.struct/position.md)
  The 3D position of the camera or viewpoint, in the simulation’s coordinate system.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Geometry and simulation inputs
- [ComputeNodeGraph.Topology](./computenodegraph/topology.md)
  The primitive topology used to assemble output geometry for an output stage.
- [enum CoordinateSpace](./coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [ComputeNodeGraph.StructureLayout](./computenodegraph/structurelayout.md)
- [enum StripOrientation](./striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct MouseParams](./mouseparams.md)
  Parameters describing mouse interaction in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/viewpoint-swift.struct)*