# SCNShadowMode.modulated

**Framework**: SceneKit  
**Kind**: case

SceneKit renders shadows by projecting the light’s [`gobo`](scnlight/gobo.md) image. The light does not illuminate the scene.

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
case modulated
```

#### Discussion

Typically, you use this mode to create a low-accuracy, high-performance shadow under a game character or similar scene element: Use an image of a radial gradient (black to white) for the light’s [`gobo`](scnlight/gobo.md) property, and use [`categoryBitMask`](scnlight/categorybitmask.md) properties to prevent the shadow image from appearing on the character.

## See Also

- [SCNShadowMode.forward](scnshadowmode/forward.md)
  SceneKit renders shadows during lighting computations.
- [SCNShadowMode.deferred](scnshadowmode/deferred.md)
  SceneKit renders shadows in a postprocessing pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadowmode/modulated)*