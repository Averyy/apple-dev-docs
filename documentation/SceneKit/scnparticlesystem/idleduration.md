# idleDuration

**Framework**: SceneKit  
**Kind**: property

The duration, in seconds, of periods when the system emits no particles. Animatable.

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
var idleDuration: CGFloat { get set }
```

#### Discussion

If the system’s [`loops`](scnparticlesystem/loops.md) property value is [`true`](https://developer.apple.com/documentation/Swift/true), you can make the system emit particles periodically or sporadically. For example, in a looping system where the [`emissionDuration`](scnparticlesystem/emissionduration.md) value is `1.0` seconds and the [`idleDuration`](scnparticlesystem/idleduration.md) value is `1.0` seconds, the system alternates between equal one-second periods of spawning and not spawning particles. You can randomize the duration with the [`idleDurationVariation`](scnparticlesystem/idledurationvariation.md) property. Idle duration has no effect if the [`loops`](scnparticlesystem/loops.md) property value is [`false`](https://developer.apple.com/documentation/Swift/false).

The default value is `0.0` seconds, specifying no idle time between emissions. (That is, if the [`loops`](scnparticlesystem/loops.md) property value is [`true`](https://developer.apple.com/documentation/Swift/true), the system emits particles continuously.)

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var emissionDuration: CGFloat](scnparticlesystem/emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](scnparticlesystem/emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDurationVariation: CGFloat](scnparticlesystem/idledurationvariation.md)
  The range, in seconds, of randomized idle duration values. Animatable.
- [var loops: Bool](scnparticlesystem/loops.md)
  A Boolean value that determines whether the system repeats its emission and idle periods.
- [var warmupDuration: CGFloat](scnparticlesystem/warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](scnparticlesystem/birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](scnparticlesystem/birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/idleduration)*