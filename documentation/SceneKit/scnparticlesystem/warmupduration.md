# warmupDuration

**Framework**: SceneKit  
**Kind**: property

The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.

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
var warmupDuration: CGFloat { get set }
```

#### Discussion

The default value is `0.0` seconds, specifying that the system begins emitting particles on the first frame SceneKit renders it in. Change this value to “fast forward” the particle system so that it appears to have been running for some amount of time when it is first rendered.

For example, consider a particle system that simulates falling snow. With the default behavior, the scene is initially clear of snowflakes, which only begin to fall as the scene appears. If you set a [`warmupDuration`](scnparticlesystem/warmupduration.md) duration of several seconds, the scene will be already filled with falling snow when it first appears.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var emissionDuration: CGFloat](scnparticlesystem/emissionduration.md)
  The duration, in seconds, over which the system spawns new particles. Animatable.
- [var emissionDurationVariation: CGFloat](scnparticlesystem/emissiondurationvariation.md)
  The range, in seconds, of randomized emission duration values. Animatable.
- [var idleDuration: CGFloat](scnparticlesystem/idleduration.md)
  The duration, in seconds, of periods when the system emits no particles. Animatable.
- [var idleDurationVariation: CGFloat](scnparticlesystem/idledurationvariation.md)
  The range, in seconds, of randomized idle duration values. Animatable.
- [var loops: Bool](scnparticlesystem/loops.md)
  A Boolean value that determines whether the system repeats its emission and idle periods.
- [var birthRate: CGFloat](scnparticlesystem/birthrate.md)
  The number of particles spawned during each emission period. Animatable.
- [var birthRateVariation: CGFloat](scnparticlesystem/birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/warmupduration)*