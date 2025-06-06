# SCNShadowMode.deferred

**Framework**: SceneKit  
**Kind**: case

SceneKit renders shadows in a postprocessing pass.

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
case deferred
```

#### Discussion

In the mode, SceneKit blends shadows into the final image after the main rendering pass, so shadows can be of any color.

## See Also

- [SCNShadowMode.forward](scnshadowmode/forward.md)
  SceneKit renders shadows during lighting computations.
- [SCNShadowMode.modulated](scnshadowmode/modulated.md)
  SceneKit renders shadows by projecting the light’s [`gobo`](scnlight/gobo.md) image. The light does not illuminate the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadowmode/deferred)*