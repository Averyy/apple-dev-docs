# SCNTransparencyMode.rgbZero

**Framework**: SceneKit  
**Kind**: case

SceneKit derives transparency information from the luminance of colors. The value `0.0` is opaque.

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
case rgbZero
```

#### Discussion

When using this mode, SceneKit ignores the alpha value of colors in the material’s [`transparent`](scnmaterial/transparent.md) property. SceneKit calculates the luminance of a color from its red, green, and blue channels and uses the resulting value to determine the material’s opacity.

## See Also

- [SCNTransparencyMode.aOne](scntransparencymode/aone.md)
  SceneKit derives transparency information from the alpha channel of colors. The value `1.0` is opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransparencymode/rgbzero)*