# idleDurationVariation

**Framework**: SceneKit  
**Kind**: property

The range, in seconds, of randomized idle duration values. Animatable.

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
var idleDurationVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`idleDuration`](scnparticlesystem/idleduration.md) property. For each idle period, SceneKit randomly adjusts the duration by up to half the [`idleDurationVariation`](scnparticlesystem/idledurationvariation.md) value. For example, if the [`idleDuration`](scnparticlesystem/idleduration.md) value is `1.0` seconds and the [`idleDurationVariation`](scnparticlesystem/idledurationvariation.md) value is `0.5` seconds, the system idles for a period of `0.75` to `1.25` seconds between emissions.

The default value is `0.0` seconds, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var emissionDuration: CGFloat](scnparticlesystem/emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](scnparticlesystem/emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDuration: CGFloat](scnparticlesystem/idleduration.md)
  The duration, in seconds, of periods when the system emits no particles. Animatable.
- [var loops: Bool](scnparticlesystem/loops.md)
  A Boolean value that determines whether the system repeats its emission and idle periods.
- [var warmupDuration: CGFloat](scnparticlesystem/warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](scnparticlesystem/birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](scnparticlesystem/birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/idledurationvariation)*