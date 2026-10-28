# SCNShadowMode.forward

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

SceneKit renders shadows during lighting computations.

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
case forward
```

```c
SCNShadowModeForward
```

## Discussion

In this mode, the color components of the light’s [`shadowColor`](../scnlight/shadowcolor.md) property do not apply. The color’s alpha component determines the intensity of shadows.

## See Also

### Constants
- [SCNShadowMode.deferred](./deferred.md)
  SceneKit renders shadows in a postprocessing pass.
- [SCNShadowMode.modulated](./modulated.md)
  SceneKit renders shadows by projecting the light’s [`gobo`](../scnlight/gobo.md) image. The light does not illuminate the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadowmode/forward)*