# birthRateVariation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The range of randomized particle birth rate values. Animatable.

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
var birthRateVariation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat birthRateVariation;
```

## Discussion

Setting a nonzero value for this property randomizes the effect of the [`birthRate`](./birthrate.md) property. For each emission period, SceneKit randomly adjusts the birth rate by up to half the [`birthRateVariation`](./birthratevariation.md) value. For example, if the [`birthRate`](./birthrate.md) value is `100` particles and the [`birthRateVariation`](./birthratevariation.md) value is `50` particles, the system randomly emits between 75 and 125 particles during its [`emissionDuration`](./emissionduration.md) period.

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
- [var idleDurationVariation: CGFloat](./idledurationvariation.md)
  The range, in seconds, of randomized idle duration values. Animatable.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether the system repeats its emission and idle periods.
- [var warmupDuration: CGFloat](./warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRate: CGFloat](./birthrate.md)
  The number of particles spawned during each emission period. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/birthratevariation)*