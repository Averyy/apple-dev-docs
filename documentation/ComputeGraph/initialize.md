# initialize

**Framework**: ComputeGraph  
**Kind**: namespace

Nodes usable within the initialization stage of an element.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Topics

### Functions
- [uint initialize::sourceElementIndex()](initialize/sourceelementindex.md)
  When initializing a new particle from an event triggered from another particle, this returns the source particle’s index with its system.
- [int initialize::spawnIndex()](initialize/spawnindex.md)
  For a derived element spawned from an emitter, returns the sequential index of the spawn from that emitter. If this was spawned from an EventSource or from the CPU, this value is the index within the current spawn request.

## See Also

- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [emitter](emitter.md)
  A set of nodes usable in the emission stage of a simulation, which control how often and how many elements to spawn.
- [force](force.md)
  Apply physics forces including gravity, drag, noise, and twist.
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
- [matrix4x4f](matrix4x4f.md)
  Transform positions and directions using matrix4x4f.
- [matrix4x4h](matrix4x4h.md)
  Transform positions and directions using matrix4x4h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/initialize)*