# numParticlesToEmit

**Framework**: SpriteKit  
**Kind**: property

The number of particles the emitter should emit before stopping.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
var numParticlesToEmit: Int { get set }
```

## Mentions

- [Creating Particle Effects](creating-particle-effects.md)

#### Discussion

The default value is `0`, which indicates that emitter creates an endless stream of particles. If a non-zero value is provided, then the emitter stops generating particles after it has created the specified number of particles.

## See Also

- [func advanceSimulationTime(TimeInterval)](skemitternode/advancesimulationtime(_:).md)
  Advances the emitter particle simulation.
- [func resetSimulation()](skemitternode/resetsimulation.md)
  Removes all existing particles and restarts the simulation.
- [var particleBirthRate: CGFloat](skemitternode/particlebirthrate.md)
  The rate at which new particles are created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/numparticlestoemit)*