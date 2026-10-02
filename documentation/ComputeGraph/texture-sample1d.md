# texture_sample1d

**Framework**: Compute Graph  
**Kind**: func

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float4 texture_sample1d(void texture, float u)
```

#### Discussion

> **Note**: ![Graph](/images/com.apple.computegraph/texture_sample1d.svg)

## See Also

- [graph](graph.md)
  A set of nodes that provide graph-wide information, such as time and coordinate-space transforms, usable in any stage.
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
- [void orient_to_velocity()](orient_to_velocity.md)
  Orient the particle by setting its `axisY` to the velocity’s current direction.
- [void gridDebugCells(grid)](griddebugcells.md)
- [void gridFromPoints(gridStorage, inputPositions, inputFlags)](gridfrompoints.md)
- [void spawn_demo()](spawn_demo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/texture_sample1d)*