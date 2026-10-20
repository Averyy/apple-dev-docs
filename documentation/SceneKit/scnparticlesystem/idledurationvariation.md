# idleDurationVariation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The range, in seconds, of randomized idle duration values. Animatable.

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
var idleDurationVariation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat idleDurationVariation;
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`idleDuration`](./idleduration.md) property. For each idle period, SceneKit randomly adjusts the duration by up to half the [`idleDurationVariation`](./idledurationvariation.md) value. For example, if the [`idleDuration`](./idleduration.md) value is `1.0` seconds and the [`idleDurationVariation`](./idledurationvariation.md) value is `0.5` seconds, the system idles for a period of `0.75` to `1.25` seconds between emissions.

The default value is `0.0` seconds, specifying no randomization.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Particle Emission Timing
- [var emissionDuration: CGFloat](./emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](./emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDuration: CGFloat](./idleduration.md)
  The duration, in seconds, of periods when the system emits no particles. Animatable.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether the system repeats its emission and idle periods.
- [var warmupDuration: CGFloat](./warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](./birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](./birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/idledurationvariation)*