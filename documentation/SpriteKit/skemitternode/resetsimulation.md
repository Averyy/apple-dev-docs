# resetSimulation()

**Framework**: SpriteKit  
**Kind**: method

Removes all existing particles and restarts the simulation.

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
func resetSimulation()
```

#### Discussion

Resetting the simulation clears the internal state of the simulation.

## See Also

- [func advanceSimulationTime(TimeInterval)](skemitternode/advancesimulationtime(_:).md)
  Advances the emitter particle simulation.
- [var particleBirthRate: CGFloat](skemitternode/particlebirthrate.md)
  The rate at which new particles are created.
- [var numParticlesToEmit: Int](skemitternode/numparticlestoemit.md)
  The number of particles the emitter should emit before stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/resetsimulation())*