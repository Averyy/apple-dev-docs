# matrix4x4f

**Framework**: ComputeGraph  
**Kind**: namespace

Transform positions and directions using matrix4x4f.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Topics

### Functions
- [float3 matrix4x4f::transformDirection(matrix, vector)](matrix4x4f/transformdirection.md)
  Transforms a direction vector by a 4x4 matrix, ignoring translation.
- [float3 matrix4x4f::transformPosition(matrix, position)](matrix4x4f/transformposition.md)
  Transforms a position by a 4x4 matrix, including translation.

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
- [random](random.md)
  Nodes for generating pseudo-random numbers.
- [matrix4x4h](matrix4x4h.md)
  Transform positions and directions using matrix4x4h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/matrix4x4f)*