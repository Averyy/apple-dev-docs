# random

**Framework**: Compute Graph  
**Kind**: namespace

Nodes for generating pseudo-random numbers.

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

- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [emitter](emitter.md)
  A set of nodes usable in the emission stage of a simulation, which control how often and how many elements to spawn.
- [force](force.md)
  Apply physics forces including gravity, drag, noise, and twist.
- [initialize](initialize.md)
  Nodes usable within the initialization stage of an element.
- [output](output.md)
  Nodes usable within the output stage of an element. You can use these nodes to change the appearance of an element without making modifications to the element itself.
- [module](module.md)
  Mutate per-particle state with operations such as setPosition, addPosition, setVelocity, setColor, setSize, and setLifetime.
- [graph](graph.md)
  A set of nodes usable in any stage within a ComputeGraph.
- [group](group.md)
  Nodes for querying the group for a current particle. Requires a system whose simulation stage is configured as either `strips` or `grouped`.
- [texture](texture.md)
  Nodes usable within the texture stage, for generating textures.
- [matrix4x4f](matrix4x4f.md)
  Transform positions and directions using matrix4x4f.
- [matrix4x4h](matrix4x4h.md)
  Transform positions and directions using matrix4x4h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random)*