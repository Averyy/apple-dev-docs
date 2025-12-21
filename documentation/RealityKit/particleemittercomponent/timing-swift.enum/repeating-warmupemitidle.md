# ParticleEmitterComponent.Timing.repeating(warmUp:emit:idle:)

**Framework**: RealityKit  
**Kind**: case

Emits for the given `emit` duration, and waits `idle` seconds before looping, `warmUp` determines how long the simulation should appear to have run before first appearing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case repeating(warmUp: TimeInterval? = nil, emit: ParticleEmitterComponent.Timing.VariableDuration, idle: ParticleEmitterComponent.Timing.VariableDuration? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/timing-swift.enum/repeating(warmup:emit:idle:))*