# birthRate

**Framework**: SceneKit  
**Kind**: property

The number of particles spawned during each emission period. Animatable.

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
var birthRate: CGFloat { get set }
```

#### Discussion

The system emits this number of particles at a constant rate through the duration of the period specified by the [`emissionDuration`](scnparticlesystem/emissionduration.md) property. A value of zero prevents the system from emitting particles, unless you randomize the birth rate with the [`birthRateVariation`](scnparticlesystem/birthratevariation.md) property.

The default value is `1`.

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
- [var warmupDuration: CGFloat](scnparticlesystem/warmupduration.md)
  The duration, in seconds, for which particles are spawned before the system is first rendered. Animatable.
- [var birthRateVariation: CGFloat](scnparticlesystem/birthratevariation.md)
  The range of randomized particle birth rate values. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/birthrate)*