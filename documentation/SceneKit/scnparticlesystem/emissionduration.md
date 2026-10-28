# emissionDuration

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The duration, in seconds, over which the system spawns new particles. Animatable.

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
var emissionDuration: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat emissionDuration;
```

## Discussion

The [`birthRate`](./birthrate.md) property determines the number of particles spawned during this duration. You can randomize the duration with the [`emissionDurationVariation`](./emissiondurationvariation.md) property.

A duration of `0.0` specifies that all particles (the value of the [`birthRate`](./birthrate.md) property) spawn instantaneously. Use this duration to create randomized static effects in your scene. For example, by combining this option with the [`birthLocation`](./birthlocation.md) and [`imageSequenceInitialFrameVariation`](./imagesequenceinitialframevariation.md) properties, you can cover a plane with a variety of sprites, creating the appearance of a grassy field.

The default value is `1.0` seconds.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Particle Emission Timing
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
- [var birthRateVariation: CGFloat](./birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/emissionduration)*