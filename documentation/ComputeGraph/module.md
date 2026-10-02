# module

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes that mutate per-particle state, including position, velocity, color, size, and lifetime.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

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
  A set of nodes for the emission stage that control how often and how many elements a simulation spawns.
- [initialize](initialize.md)
  A set of nodes for the initialization stage that set an element’s starting state.
- [output](output.md)
  A set of nodes for the output stage that adjust an element’s appearance without modifying its underlying state.
- [force](force.md)
  A set of nodes that apply physics forces to particles, including gravity, drag, noise, and twist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/module)*