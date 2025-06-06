# MDLMaterialTextureWrapMode.clamp

**Framework**: Model I/O  
**Kind**: case

Sampling at any texture coordinate outside the `0.0` to `1.0` range returns the texel color from the nearest edge.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case clamp
```

## See Also

- [MDLMaterialTextureWrapMode.repeat](mdlmaterialtexturewrapmode/repeat.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a repeated tiling effect.
- [MDLMaterialTextureWrapMode.mirror](mdlmaterialtexturewrapmode/mirror.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a mirrored tiling effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode/clamp)*