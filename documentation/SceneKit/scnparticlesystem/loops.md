# loops

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the system repeats its emission and idle periods.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var loops: Bool { get set }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/swift/true) (the default), you can make the system emit particles periodically or sporadically. For example, in a looping system where the [`emissionDuration`](scnparticlesystem/emissionduration.md) value is `1.0` seconds and the [`idleDuration`](scnparticlesystem/idleduration.md) value is `1.0` seconds, the system alternates alternates between equal one-second periods of spawning and not spawning particles. Use the [`emissionDurationVariation`](scnparticlesystem/emissiondurationvariation.md) and [`idleDurationVariation`](scnparticlesystem/idledurationvariation.md) properties to randomize the duration of each emission and idle period, making the emission behavior more sporadic.

Specify [`false`](https://developer.apple.com/documentation/swift/false) for particle systems that create one-shot effects, such as an explosion that appears when a game character is defeated.

## See Also

- [var emissionDuration: CGFloat](scnparticlesystem/emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](scnparticlesystem/emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDuration: CGFloat](scnparticlesystem/idleduration.md)
  The duration, in seconds, of periods when the system emits no particles. Animatable.
- [var idleDurationVariation: CGFloat](scnparticlesystem/idledurationvariation.md)
  The range, in seconds, of randomized idle duration values. Animatable.
- [var warmupDuration: CGFloat](scnparticlesystem/warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](scnparticlesystem/birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](scnparticlesystem/birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/loops)*