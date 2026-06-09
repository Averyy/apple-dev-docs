# module

**Framework**: ComputeGraph  
**Kind**: namespace

Mutate per-particle state with operations such as setPosition, addPosition, setVelocity, setColor, setSize, and setLifetime.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Topics

### Namespaces
- [module::debug](module/debug.md)
### Functions
- [void module::addPosition(offset)](module/addposition.md)
  Moves an element by adding an offset to its current position.
- [void module::addVelocity(velocity)](module/addvelocity.md)
  Adds a velocity delta to the element’s current velocity.
- [void module::setAlpha(alpha)](module/setalpha.md)
  Sets the alpha (opacity) value of an element.
- [void module::setColor(color)](module/setcolor.md)
  Sets the color of an element to the specified RGBA value.
- [void module::setLifetime(lifetime)](module/setlifetime.md)
  Sets the lifetime of an element in seconds.
- [void module::setPosition(position)](module/setposition.md)
  Sets the position of an element to the specified coordinates.
- [void module::setSize(size)](module/setsize.md)
  Sets the size of an element to the specified dimensions. Size is in meters.
- [void module::setVelocity(velocity)](module/setvelocity.md)
  Sets the velocity of an element to the specified value.

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

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/module)*