# numParticlesToEmit

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The number of particles the emitter should emit before stopping.

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
var numParticlesToEmit: Int { get set }
```

```objc
@property (nonatomic) NSUInteger numParticlesToEmit;
```

## Mentions

- [Creating Particle Effects](../creating-particle-effects.md)

## Discussion

The default value is `0`, which indicates that emitter creates an endless stream of particles. If a non-zero value is provided, then the emitter stops generating particles after it has created the specified number of particles.

## See Also

### Controlling When Particles Are Created
- [func advanceSimulationTime(TimeInterval)](./advancesimulationtime%28_%29.md)
  Advances the emitter particle simulation.
- [func resetSimulation()](./resetsimulation%28%29.md)
  Removes all existing particles and restarts the simulation.
- [var particleBirthRate: CGFloat](./particlebirthrate.md)
  The rate at which new particles are created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/numparticlestoemit)*