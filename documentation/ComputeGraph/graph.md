# graph

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes usable in any stage within a ComputeGraph.

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
- [group](group.md)
  Nodes for querying the group for a current particle. Requires a system whose simulation stage is configured as either `strips` or `grouped`.
- [texture](texture.md)
  Nodes usable within the texture stage, for generating textures.
- [random](random.md)
  Nodes for generating pseudo-random numbers.
- [matrix4x4f](matrix4x4f.md)
  Transform positions and directions using matrix4x4f.
- [matrix4x4h](matrix4x4h.md)
  Transform positions and directions using matrix4x4h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/graph)*