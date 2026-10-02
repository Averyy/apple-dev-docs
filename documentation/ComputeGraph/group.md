# group

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes for querying the group of the current particle. Available only when the simulation uses a grouped or strips element grouping.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Topics

### Functions
- [int group::elementActiveInGroup()](group/elementactiveingroup.md)
  Returns the number of currently active elements in the group.
- [int group::elementIndexInGroup()](group/elementindexingroup.md)
  Returns the index of the current element within its group.
- [int group::elementMaximumInGroup()](group/elementmaximumingroup.md)
  Returns the maximum number of elements that can exist in the group.
- [int group::groupIndexInSystem()](group/groupindexinsystem.md)
  Returns the index of the current group within the particle system.
- [int group::maximumGroupsInSystem()](group/maximumgroupsinsystem.md)
  Returns the maximum number of groups allowed in the particle system.

## See Also

- [graph](graph.md)
  A set of nodes that provide graph-wide information, such as time and coordinate-space transforms, usable in any stage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/group)*