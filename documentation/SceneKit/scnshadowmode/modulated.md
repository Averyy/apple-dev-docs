# SCNShadowMode.modulated

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

SceneKit renders shadows by projecting the light’s [`gobo`](../scnlight/gobo.md) image. The light does not illuminate the scene.

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
case modulated
```

```c
SCNShadowModeModulated
```

## Discussion

Typically, you use this mode to create a low-accuracy, high-performance shadow under a game character or similar scene element: Use an image of a radial gradient (black to white) for the light’s [`gobo`](../scnlight/gobo.md) property, and use [`categoryBitMask`](../scnlight/categorybitmask.md) properties to prevent the shadow image from appearing on the character.

## See Also

### Constants
- [SCNShadowMode.forward](./forward.md)
  SceneKit renders shadows during lighting computations.
- [SCNShadowMode.deferred](./deferred.md)
  SceneKit renders shadows in a postprocessing pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadowmode/modulated)*