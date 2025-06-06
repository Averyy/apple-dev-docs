# rWrapMode

**Framework**: Model I/O  
**Kind**: property

The coordinate wrapping mode for texture r-coordinates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rWrapMode: MDLMaterialTextureWrapMode { get set }
```

#### Discussion

Texture coordinates canonically range from `0.0` to `1.0`; wrap mode determines the behavior for samples from outside that range. For details, see [`MDLMaterialTextureWrapMode`](mdlmaterialtexturewrapmode.md).

The r-coordinate is the third value in a set of texture coordinates, used only with three-dimensional textures.

## See Also

- [var sWrapMode: MDLMaterialTextureWrapMode](mdltexturefilter/swrapmode.md)
  The coordinate wrapping mode for texture t-coordinates.
- [var tWrapMode: MDLMaterialTextureWrapMode](mdltexturefilter/twrapmode.md)
  The coordinate wrapping mode for texture t-coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturefilter/rwrapmode)*