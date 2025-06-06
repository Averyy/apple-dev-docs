# generatingNormalMap()

**Framework**: SpriteKit  
**Kind**: method

Creates a normal map texture by analyzing the contents of an existing texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func generatingNormalMap() -> Self
```

#### Return Value

A new texture object that contains a normal map.

#### Discussion

A normal map texture is similar to an image texture, but instead of holding image data to be displayed onscreen, every texel represents a normal vector. Normal map textures are used to simulate 3D lighting (see the [`normalTexture`](skspritenode/normaltexture.md) property) or used to generate velocity values (see [`velocityField(with:)`](skfieldnode/velocityfield(with:).md)).

You can create normal maps in two different ways. First, you can take an existing image map and use it to generate a normal map. SpriteKit filters the color data in the texture and then uses it to generate a map based on pixel contrast. Alternatively, you can load a regular image file but treat it as a normal map. To do this, provide a texture with 32-bit `RGBx` pixel data. Each component’s 8-bit integer value is mapped to a floating point number between the values of `-1.0` and `1.0`. Use a `0` to represent `-1.0f`, a value of `127` to represent `0.0`, and a value of `255` to represent `+1.0`.

The image below shows two sprite nodes both with the same texture. The node on the right has a normal map from the same noise texture generated using the [`generatingNormalMap()`](sktexture/generatingnormalmap().md) method.

![Comparison of sprites with and without normal mapping](https://docs-assets.developer.apple.com/published/fb984f97fc198fed309be79f120384d7/media-3020491%402x.png)

## See Also

- [func generatingNormalMap(withSmoothness: CGFloat, contrast: CGFloat) -> Self](sktexture/generatingnormalmap(withsmoothness:contrast:).md)
  Creates a normal map texture by analyzing the contents of an existing texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/generatingnormalmap())*