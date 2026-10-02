# viewpoint

**Framework**: Compute Graph  
**Kind**: func

Returns the current viewpoint, if one is provided.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
Viewpoint viewpoint()
```

#### Discussion

Depending on context, this may include direction, position, or both values. On visionOS, a `ParticleViewpoint` component needs to be added to the scene to automatically provide this value.

> **Note**: ![Graph](/images/com.apple.computegraph/viewpoint.svg)

> **Note**: Reads from shared uniform Viewpoint

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
- [void element_integrate()](element_integrate.md)
- [float4 texture_sample(texture, uv)](texture_sample.md)
- [float4 texture_sample1d(texture, u)](texture_sample1d.md)
- [void orient_to_velocity()](orient_to_velocity.md)
  Orient the particle by setting its `axisY` to the velocity’s current direction.
- [void gridDebugCells(grid)](griddebugcells.md)
- [void gridFromPoints(gridStorage, inputPositions, inputFlags)](gridfrompoints.md)
- [void spawn_demo()](spawn_demo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/viewpoint-swift.func)*