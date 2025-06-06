# HMCharacteristicTypeHue

**Framework**: HomeKit  
**Kind**: var

The hue of the color used by a light.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeHue: String
```

#### Discussion

The corresponding value is a floating point number in units of arc degrees. Values range from 0 to 360, representing the color spectrum starting from red, through yellow, green, cyan, blue, and finally magenta, before wrapping back to red.

## See Also

- [let HMCharacteristicTypeCurrentLightLevel: String](hmcharacteristictypecurrentlightlevel.md)
  The current light level.
- [let HMCharacteristicTypeBrightness: String](hmcharacteristictypebrightness.md)
  The brightness of a light.
- [let HMCharacteristicTypeSaturation: String](hmcharacteristictypesaturation.md)
  The saturation of the color used by a light.
- [let HMCharacteristicTypeColorTemperature: String](hmcharacteristictypecolortemperature.md)
  The color temperature of a light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypehue)*