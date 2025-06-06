# irradianceTextureCube(with:name:dimensions:)

**Framework**: Model I/O  
**Kind**: method

Generates an irradiance texture from the specified reflectance cube texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func irradianceTextureCube(with texture: MDLTexture, name: String?, dimensions: vector_int2) -> Self
```

#### Return Value

A new cube texture object.

#### Discussion

Irradiance and reflectance textures are used in realistic lighting:

- A reflectance texture, also known as an environment map, contains a rendering of a scene as seen from a specific position. A renderer can use this texture to create reflections on surfaces with metallic materials.
- An irradiance contains samples of the total light arriving at the a specific position from every direction. A renderer can use this texture to create diffuse lighting effects.

Typically, an irradiance texture is derived from a reflective texture. For example, consider a reflective texture that is red in all directions above its position and blue in all directions below that point. The side of an object rendered with a reflective material would show a hard line between red and blue, but a diffuse material should appear purple, because the side of the object receives a blend of the red light from above and the blue light from below. Therefore, this method generates an irradiance texture that is red directly above, is blue directly below, and contains gradations of purple on all sides.

Calling this method is equivalent to calling the [`irradianceTextureCube(with:name:dimensions:roughness:)`](mdltexture/irradiancetexturecube(with:name:dimensions:roughness:).md) method with the `roughness` value automatically varying from `0.0` at the largest mip level to `1.0` at the smallest.

You can use reflective and irradiance textures with the [`MDLLightProbe`](mdllightprobe.md) class.

## Parameters

- `texture`: The reflective (environment map) cube texture from which to generate an irradiance texture.
- `name`: The   property for the newly generated texture.
- `dimensions`: The size (width and height in texels) of each cube face for the newly generated texture.

## See Also

- [class func irradianceTextureCube(with: MDLTexture, name: String?, dimensions: vector_int2, roughness: Float) -> Self](mdltexture/irradiancetexturecube(with:name:dimensions:roughness:).md)
  Generates an irradiance texture from the specified reflectance cube texture, assuming a surface of the specified roughness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/irradiancetexturecube(with:name:dimensions:))*