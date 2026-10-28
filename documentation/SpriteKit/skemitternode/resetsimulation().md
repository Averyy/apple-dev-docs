# resetSimulation()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Removes all existing particles and restarts the simulation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func resetSimulation()
```

```objc
- (void) resetSimulation;
```

## Discussion

Resetting the simulation clears the internal state of the simulation.

## See Also

### Controlling When Particles Are Created
- [func advanceSimulationTime(TimeInterval)](./advancesimulationtime%28_%29.md)
  Advances the emitter particle simulation.
- [var particleBirthRate: CGFloat](./particlebirthrate.md)
  The rate at which new particles are created.
- [var numParticlesToEmit: Int](./numparticlestoemit.md)
  The number of particles the emitter should emit before stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/resetsimulation())*