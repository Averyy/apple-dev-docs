# MDLMaterialTextureWrapMode.mirror

**Framework**: Model I/O  
**Kind**: case

Sampling at texture coordinates outside the `0.0` to `1.0` range results in a mirrored tiling effect.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case mirror
```

#### Discussion

This effect is similar to that of the [`MDLMaterialTextureWrapMode.repeat`](mdlmaterialtexturewrapmode/repeat.md) mode, but inverts the range of fractional texture coordinate values whenever the whole part of a texture coordinate value is odd. For example, sampling at a coordinate value of `1.7` or `5.7` returns the texel color for the coordinate value of `0.3` (because `1.0 - 0.7 = 0.3`), and sampling at a coordinate value of `2.7` or `8.7` returns the texel color for the coordinate value of `0.7`. The visual effect of this mode is to repeat the texture image endlessly across a surface rendered with the texture, with every other repetition in a mirrored orientation.

## See Also

- [MDLMaterialTextureWrapMode.clamp](mdlmaterialtexturewrapmode/clamp.md)
  Sampling at any texture coordinate outside the `0.0` to `1.0` range returns the texel color from the nearest edge.
- [MDLMaterialTextureWrapMode.repeat](mdlmaterialtexturewrapmode/repeat.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a repeated tiling effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode/mirror)*