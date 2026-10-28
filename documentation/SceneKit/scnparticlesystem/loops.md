# loops

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the system repeats its emission and idle periods.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var loops: Bool { get set }
```

```objc
@property (nonatomic) BOOL loops;
```

## Discussion

If this value is [`true`](../../Swift/true.md) (the default), you can make the system emit particles periodically or sporadically. For example, in a looping system where the [`emissionDuration`](./emissionduration.md) value is `1.0` seconds and the [`idleDuration`](./idleduration.md) value is `1.0` seconds, the system alternates alternates between equal one-second periods of spawning and not spawning particles. Use the [`emissionDurationVariation`](./emissiondurationvariation.md) and [`idleDurationVariation`](./idledurationvariation.md) properties to randomize the duration of each emission and idle period, making the emission behavior more sporadic.

Specify [`false`](../../Swift/false.md) for particle systems that create one-shot effects, such as an explosion that appears when a game character is defeated.

## See Also

### Managing Particle Emission Timing
- [var emissionDuration: CGFloat](./emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](./emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDuration: CGFloat](./idleduration.md)
  The duration, in seconds, of periods when the system emits no particles. Animatable.
- [var idleDurationVariation: CGFloat](./idledurationvariation.md)
  The range, in seconds, of randomized idle duration values. Animatable.
- [var warmupDuration: CGFloat](./warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](./birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](./birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/loops)*