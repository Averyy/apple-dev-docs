# init(colorTemperatureGradientFrom:toColorTemperature:name:textureDimensions:)

**Framework**: Model I/O  
**Kind**: init

Initializes a texture that creates a vertical gradient between two color temperatures.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(colorTemperatureGradientFrom colorTemperature1: Float, toColorTemperature colorTemperature2: Float, name: String?, textureDimensions: vector_int2)
```

#### Return Value

A new color swatch texture object.

#### Discussion

Real-world light sources often measure color of illumination based on a black-body temperature scale. For example, the colors and characterizations of typical home and office light fixtures correspond to the following temperatures:

| Label | Color | Temperature |
| --- | --- | --- |
| “Soft white” | Warm, yellowish white | 2700 K |
| “Bright white” | Pale yellowish white | 3000 K |
| “Daylight” | Bright, slightly greenish white | 5000 K |
| “Cool daylight” | Bright, slightly bluish white | 6500 K |

This initializer does not generate texel data; the [`MDLColorSwatchTexture`](mdlcolorswatchtexture.md) class automatically generates data and caches it for reuse when you use one of the [`MDLTexture`](mdltexture.md) methods listed in Accessing Texture Data.

## Parameters

- `colorTemperature1`: The black-body color temperature, in Kelvins, at the top of the gradient.
- `colorTemperature2`: The black-body color temperature, in Kelvins, at the bottom of the gradient.
- `name`: The   property for the new texture object.
- `textureDimensions`: The texel dimensions (width and height) of the texture image.

## See Also

- [init(colorGradientFrom: CGColor, to: CGColor, name: String?, textureDimensions: vector_int2)](mdlcolorswatchtexture/init(colorgradientfrom:to:name:texturedimensions:).md)
  Initializes a texture that creates a vertical gradient between two colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcolorswatchtexture/init(colortemperaturegradientfrom:tocolortemperature:name:texturedimensions:))*