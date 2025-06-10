# SCNParticleSortingMode.oldestFirst

**Framework**: SceneKit  
**Kind**: case

Particles emitted earlier are rendered before particles emitted more recently.

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
case oldestFirst
```

## See Also

- [SCNParticleSortingMode.none](scnparticlesortingmode/none.md)
  Particles are not sorted; they may be rendered in any order.
- [SCNParticleSortingMode.projectedDepth](scnparticlesortingmode/projecteddepth.md)
  Particles farther from the point of view (as measured using projected depth) are rendered before closer particles.
- [SCNParticleSortingMode.distance](scnparticlesortingmode/distance.md)
  Particles farther from the point of view (as measured using distance from the camera in scene space) are rendered before closer particles.
- [SCNParticleSortingMode.youngestFirst](scnparticlesortingmode/youngestfirst.md)
  Particles emitted more recently are rendered before particles emitted earlier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode/oldestfirst)*