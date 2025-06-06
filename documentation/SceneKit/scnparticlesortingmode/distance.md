# SCNParticleSortingMode.distance

**Framework**: SceneKit  
**Kind**: case

Particles farther from the point of view (as measured using distance from the camera in scene space) are rendered before closer particles.

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
case distance
```

#### Discussion

Typically you use this sorting mode in conjunction with the [`SCNParticleOrientationMode.billboardViewAligned`](scnparticleorientationmode/billboardviewaligned.md) orientation mode.

## See Also

- [SCNParticleSortingMode.none](scnparticlesortingmode/none.md)
  Particles are not sorted; they may be rendered in any order.
- [SCNParticleSortingMode.projectedDepth](scnparticlesortingmode/projecteddepth.md)
  Particles farther from the point of view (as measured using projected depth) are rendered before closer particles.
- [SCNParticleSortingMode.oldestFirst](scnparticlesortingmode/oldestfirst.md)
  Particles emitted earlier are rendered before particles emitted more recently.
- [SCNParticleSortingMode.youngestFirst](scnparticlesortingmode/youngestfirst.md)
  Particles emitted more recently are rendered before particles emitted earlier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/distance)*