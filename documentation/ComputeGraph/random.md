# random

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes that generate pseudo-random scalars and vectors.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Topics

### Functions
- [float2 random::float2_01()](random/float2_01.md)
  Generates a pseudo-random 2D vector with single-precision components between 0 and 1.
- [float2 random::float2_01_using(seed)](random/float2_01_using.md)
  Generates a pseudo-random 2D vector with single-precision components between 0 and 1 using a specific seed.
- [float3 random::float3_01()](random/float3_01.md)
  Generates a pseudo-random 3D vector with single-precision components between 0 and 1.
- [float3 random::float3_01_using(seed)](random/float3_01_using.md)
  Generates a pseudo-random 3D vector with single-precision components between 0 and 1 using a specific seed.
- [float4 random::float4_01()](random/float4_01.md)
  Generates a pseudo-random 4D vector with single-precision components between 0 and 1.
- [float4 random::float4_01_using(seed)](random/float4_01_using.md)
  Generates a pseudo-random 4D vector with single-precision components between 0 and 1 using a specific seed.
- [float random::float_01()](random/float_01.md)
  Generates a pseudo-random single-precision float between 0 and 1.
- [float random::float_01_using(seed)](random/float_01_using.md)
  Generates a pseudo-random single-precision float between 0 and 1 using a specific seed.
- [half2 random::half2_01()](random/half2_01.md)
  Generates a pseudo-random 2D vector with half-precision components between 0 and 1.
- [half2 random::half2_01_using(seed)](random/half2_01_using.md)
  Generates a pseudo-random 2D vector with half-precision components between 0 and 1 using a specific seed.
- [half3 random::half3_01()](random/half3_01.md)
  Generates a pseudo-random 3D vector with half-precision components between 0 and 1.
- [half3 random::half3_01_using(seed)](random/half3_01_using.md)
  Generates a pseudo-random 3D vector with half-precision components between 0 and 1 using a specific seed.
- [half4 random::half4_01()](random/half4_01.md)
  Generates a pseudo-random 4D vector with half-precision components between 0 and 1.
- [half4 random::half4_01_using(seed)](random/half4_01_using.md)
  Generates a pseudo-random 4D vector with half-precision components between 0 and 1 using a specific seed.
- [half random::half_01()](random/half_01.md)
  Generates a pseudo-random half-precision float between 0 and 1.
- [half random::half_01_using(seed)](random/half_01_using.md)
  Generates a pseudo-random half-precision float between 0 and 1 using a specific seed.
- [uint random::integer()](random/integer.md)
  Generates a pseudo-random 32-bit unsigned integer.
- [uint random::integer_using(seed)](random/integer_using.md)
  Generates a pseudo-random 32-bit unsigned integer using a specific seed.
- [uint random::seed()](random/seed.md)
  Returns the current random seed, without incrementing it.

## See Also

- [graph](graph.md)
  A set of nodes that provide graph-wide information, such as time and coordinate-space transforms, usable in any stage.
- [group](group.md)
  A set of nodes for querying the group of the current particle. Available only when the simulation uses a grouped or strips element grouping.
- [texture](texture.md)
  A set of nodes for the texture stage that sample and generate texture data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random)*