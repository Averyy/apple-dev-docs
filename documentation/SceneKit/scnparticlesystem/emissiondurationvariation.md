# emissionDurationVariation

**Framework**: SceneKit  
**Kind**: property

The range, in seconds, of randomized emission duration values. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var emissionDurationVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`emissionDuration`](scnparticlesystem/emissionduration.md) property. For each emission period, SceneKit randomly adjusts the duration by up to half the [`emissionDurationVariation`](scnparticlesystem/emissiondurationvariation.md) value. For example, if the [`emissionDuration`](scnparticlesystem/emissionduration.md) value is `1.0` seconds and the [`emissionDurationVariation`](scnparticlesystem/emissiondurationvariation.md) value is `0.5` seconds, the system emits particles over a period of `0.75` to `1.25` seconds before stopping.

The default value is `0.0` seconds, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var emissionDuration: CGFloat](scnparticlesystem/emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var idleDuration: CGFloat](scnparticlesystem/idleduration.md)
  The duration, in seconds, of periods when the system emits no particles. Animatable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/emissiondurationvariation)*