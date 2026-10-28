# idleDuration

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The duration, in seconds, of periods when the system emits no particles. Animatable.

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
var idleDuration: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat idleDuration;
```

## Discussion

If the system’s [`loops`](./loops.md) property value is [`true`](../../Swift/true.md), you can make the system emit particles periodically or sporadically. For example, in a looping system where the [`emissionDuration`](./emissionduration.md) value is `1.0` seconds and the [`idleDuration`](./idleduration.md) value is `1.0` seconds, the system alternates between equal one-second periods of spawning and not spawning particles. You can randomize the duration with the [`idleDurationVariation`](./idledurationvariation.md) property. Idle duration has no effect if the [`loops`](./loops.md) property value is [`false`](../../Swift/false.md).

The default value is `0.0` seconds, specifying no idle time between emissions. (That is, if the [`loops`](./loops.md) property value is [`true`](../../Swift/true.md), the system emits particles continuously.)

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Particle Emission Timing
- [var emissionDuration: CGFloat](./emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](./emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDurationVariation: CGFloat](./idledurationvariation.md)
  The range, in seconds, of randomized idle duration values. Animatable.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether the system repeats its emission and idle periods.
- [var warmupDuration: CGFloat](./warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](./birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](./birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/idleduration)*