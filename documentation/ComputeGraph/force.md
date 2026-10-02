# force

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes that apply physics forces to particles, including gravity, drag, noise, and twist.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Topics

### Functions
- [void force::add(force)](force/add.md)
  Adds a constant force vector to the current element.
- [void force::drag(linearDragFactor)](force/drag.md)
  Applies linear drag to slow down the current element over time.
- [void force::gravity(gravity)](force/gravity.md)
  Applies a gravity force to the current element
- [void force::noise(params)](force/noise.md)
  Applies a noise force to the current element
- [void force::twist(origin, strength, attraction)](force/twist.md)
  Applies a twisting force around a vertical axis through a specified origin point.

## See Also

- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [emitter](emitter.md)
  A set of nodes for the emission stage that control how often and how many elements a simulation spawns.
- [initialize](initialize.md)
  A set of nodes for the initialization stage that set an element’s starting state.
- [module](module.md)
  A set of nodes that mutate per-particle state, including position, velocity, color, size, and lifetime.
- [output](output.md)
  A set of nodes for the output stage that adjust an element’s appearance without modifying its underlying state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/force)*