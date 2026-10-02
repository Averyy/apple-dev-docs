# emitter

**Framework**: Compute Graph  
**Kind**: namespace

A set of nodes for the emission stage that control how often and how many elements a simulation spawns.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Topics

### Functions
- [void emitter::burst(burstSize)](emitter/burst.md)
  Emit a single burst of particles when the system spawns.
- [void emitter::continuous(rate, maxBurst)](emitter/continuous.md)
  Continuously emit particles at a fixed rate.
- [void emitter::periodicBurst(intervalRange, burstSize)](emitter/periodicburst.md)
  Emit a burst of particles periodically.
- [void emitter::setGroup(activeGroup, sequentialGroups)](emitter/setgroup.md)
  Sets the element group(s) for spawn requests from this emitter.

## See Also

- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [initialize](initialize.md)
  A set of nodes for the initialization stage that set an element’s starting state.
- [module](module.md)
  A set of nodes that mutate per-particle state, including position, velocity, color, size, and lifetime.
- [output](output.md)
  A set of nodes for the output stage that adjust an element’s appearance without modifying its underlying state.
- [force](force.md)
  A set of nodes that apply physics forces to particles, including gravity, drag, noise, and twist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/emitter)*