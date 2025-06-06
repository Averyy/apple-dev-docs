# lightCubeMap

**Framework**: Model I/O  
**Kind**: property

A cube map texture describing the light’s intensity in all directions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lightCubeMap: MDLTexture? { get }
```

#### Discussion

Use the [`generateSphericalHarmonics(fromLight:)`](mdlphotometriclight/generatesphericalharmonics(fromlight:).md) method to create a cube map texture based on the light’s photometry data, then use this property to access the resulting texture. In this texture, each texel represents the light’s intensity in the direction from the cube’s center to the texel’s position on the cube.

## See Also

- [func generateCubemap(fromLight: Int)](mdlphotometriclight/generatecubemap(fromlight:).md)
  Generates a cube map texture from the light’s photometry data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphotometriclight/lightcubemap)*