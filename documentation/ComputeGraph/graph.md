# graph

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes that provide graph-wide information, such as time and coordinate-space transforms, usable in any stage.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Topics

### Functions
- [float graph::age()](graph/age.md)
  Returns the age of the graph in seconds.
- [float graph::deltaTime()](graph/deltatime.md)
  Returns the time elapsed since the last frame.
- [float4x4 graph::localToWorld()](graph/localtoworld.md)
  Returns the transformation matrix from local space to world space.
- [float4x4 graph::worldToLocal()](graph/worldtolocal.md)
  Returns the transformation matrix from world space to local space.

## See Also

- [group](group.md)
  A set of nodes for querying the group of the current particle. Available only when the simulation uses a grouped or strips element grouping.
- [texture](texture.md)
  A set of nodes for the texture stage that sample and generate texture data.
- [random](random.md)
  A set of nodes that generate pseudo-random scalars and vectors.
- [matrix4x4f](matrix4x4f.md)
  A set of nodes that transform positions and directions with single-precision 4×4 matrices.
- [matrix4x4h](matrix4x4h.md)
  A set of nodes that transform positions and directions with half-precision 4×4 matrices.
- [Viewpoint viewpoint()](viewpoint-swift.func.md)
  Returns the current viewpoint, if one is provided.
- [void element_integrate()](element_integrate.md)
- [float4 texture_sample(texture, uv)](texture_sample.md)
- [float4 texture_sample1d(texture, u)](texture_sample1d.md)
- [void orient_to_velocity()](orient_to_velocity.md)
  Orient the particle by setting its `axisY` to the velocity’s current direction.
- [void gridDebugCells(grid)](griddebugcells.md)
- [void gridFromPoints(gridStorage, inputPositions, inputFlags)](gridfrompoints.md)
- [void spawn_demo()](spawn_demo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/graph)*