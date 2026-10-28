# generateCubemap(fromLight:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Generates a cube map texture from the light’s photometry data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func generateCubemap(fromLight textureSize: Int)
```

```objc
- (void) generateCubemapFromLight:(NSUInteger) textureSize;
```

## Discussion

After generating a texture, use the [`lightCubeMap`](./lightcubemap.md) property to access it. In this texture, each texel represents the light’s intensity in the direction from the cube’s center to the texel’s position on the cube.

## Parameters

- `textureSize`: The size (side length in pixels) of cube map texture to generate.

## See Also

### Interpreting the Light Web as a Cube Texture
- [var lightCubeMap: MDLTexture?](./lightcubemap.md)
  A cube map texture describing the light’s intensity in all directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphotometriclight/generatecubemap(fromlight:))*