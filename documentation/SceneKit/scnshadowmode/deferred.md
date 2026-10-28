# SCNShadowMode.deferred

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

SceneKit renders shadows in a postprocessing pass.

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
case deferred
```

```c
SCNShadowModeDeferred
```

## Discussion

In the mode, SceneKit blends shadows into the final image after the main rendering pass, so shadows can be of any color.

## See Also

### Constants
- [SCNShadowMode.forward](./forward.md)
  SceneKit renders shadows during lighting computations.
- [SCNShadowMode.modulated](./modulated.md)
  SceneKit renders shadows by projecting the light’s [`gobo`](../scnlight/gobo.md) image. The light does not illuminate the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadowmode/deferred)*