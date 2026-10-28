# warmupDuration

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.

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
var warmupDuration: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat warmupDuration;
```

## Discussion

The default value is `0.0` seconds, specifying that the system begins emitting particles on the first frame SceneKit renders it in. Change this value to “fast forward” the particle system so that it appears to have been running for some amount of time when it is first rendered.

For example, consider a particle system that simulates falling snow. With the default behavior, the scene is initially clear of snowflakes, which only begin to fall as the scene appears. If you set a [`warmupDuration`](./warmupduration.md) duration of several seconds, the scene will be already filled with falling snow when it first appears.

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
- [var birthRate: CGFloat](./birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](./birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/warmupduration)*