# init(name:channelEncoding:textureDimensions:turbidity:sunElevation:upperAtmosphereScattering:groundAlbedo:)

**Framework**: Model I/O  
**Kind**: init

Initializes a sky cube texture object with the specified parameters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(name: String?, channelEncoding: MDLTextureChannelEncoding, textureDimensions: vector_int2, turbidity: Float, sunElevation: Float, upperAtmosphereScattering: Float, groundAlbedo: Float)
```

#### Return Value

A new sky cube texture object.

#### Discussion

The newly created texture is a cube texture; that is, its [`isCube`](mdltexture/iscube.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), and its [`dimensions`](mdltexture/dimensions.md) property reflects the vertical layout of cube faces.

This initializer does not generate texel data; the [`MDLSkyCubeTexture`](mdlskycubetexture.md) class automatically generates data and caches it for reuse when you use one of the [`MDLTexture`](mdltexture.md) methods listed in Accessing Texture Data.

## Parameters

- `name`: The   property for the new texture object.
- `channelEncoding`: The data format for each channel value per texel—for example, 8-bit integer or 32-bit floating point. For possible values, see  .
- `textureDimensions`: The texel dimensions (width and height) of the texture image.
- `turbidity`: The cloudiness or haziness of the simulated sky. See the   property.
- `sunElevation`: The sun’s position in the simulated sky. See the   property.
- `upperAtmosphereScattering`: A factor that influences the color of the simulated sky. See the   property.
- `groundAlbedo`: A factor that influences the clarity of the simulated sky. See the   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/init(name:channelencoding:texturedimensions:turbidity:sunelevation:upperatmospherescattering:groundalbedo:))*