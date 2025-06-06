# init(byGeneratingNormalMapWith:name:smoothness:contrast:)

**Framework**: Model I/O  
**Kind**: init

Initializes a normal map to be generated from the specified texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(byGeneratingNormalMapWith sourceTexture: MDLTexture, name: String?, smoothness: Float, contrast: Float)
```

#### Return Value

A new normal map texture object.

#### Discussion

This initializer does not generate texel data; the [`MDLNormalMapTexture`](mdlnormalmaptexture.md) class automatically generates data when you use one of the [`MDLTexture`](mdltexture.md) methods listed in Accessing Texture Data. The generated texture uses the same dimensions and other properties as the source texture.

## Parameters

- `sourceTexture`: The texture from which to generate a normal map.
- `name`: The   property for the new texture object.
- `smoothness`: A number between   and   indicating how much the texture should be smoothed before the normal map is generated. A value of   means that the texture is not smoothed at all before being processed.
- `contrast`: A value used to magnify the effect of the generated normal map. A value of   indicates no magnification is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnormalmaptexture/init(bygeneratingnormalmapwith:name:smoothness:contrast:))*