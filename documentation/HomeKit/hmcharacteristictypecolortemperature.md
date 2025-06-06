# HMCharacteristicTypeColorTemperature

**Framework**: HomeKit  
**Kind**: var

The color temperature of a light.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let HMCharacteristicTypeColorTemperature: String
```

#### Discussion

The corresponding value is an integer representing the color temperature in micro-reciprocal degrees (mired), which is 1,000,000 divided by the color temperature in kelvins. For example, to emulate a traditional tungsten light with a color temperature of 3200 K, use a mired value of about 312.

## See Also

- [let HMCharacteristicTypeCurrentLightLevel: String](hmcharacteristictypecurrentlightlevel.md)
  The current light level.
- [let HMCharacteristicTypeHue: String](hmcharacteristictypehue.md)
  The hue of the color used by a light.
- [let HMCharacteristicTypeBrightness: String](hmcharacteristictypebrightness.md)
  The brightness of a light.
- [let HMCharacteristicTypeSaturation: String](hmcharacteristictypesaturation.md)
  The saturation of the color used by a light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypecolortemperature)*