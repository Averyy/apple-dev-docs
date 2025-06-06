# SCNTransparencyMode.rgbZero

**Framework**: SceneKit  
**Kind**: case

SceneKit derives transparency information from the luminance of colors. The value `0.0` is opaque.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case rgbZero
```

#### Discussion

When using this mode, SceneKit ignores the alpha value of colors in the material’s [`transparent`](scnmaterial/transparent.md) property. SceneKit calculates the luminance of a color from its red, green, and blue channels and uses the resulting value to determine the material’s opacity.

## See Also

- [SCNTransparencyMode.aOne](scntransparencymode/aone.md)
  SceneKit derives transparency information from the alpha channel of colors. The value `1.0` is opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransparencymode/rgbzero)*