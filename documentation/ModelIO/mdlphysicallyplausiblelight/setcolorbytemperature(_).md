# setColorByTemperature(_:)

**Framework**: Model I/O  
**Kind**: method

Sets the light’s color based on a black-body temperature.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setColorByTemperature(_ temperature: Float)
```

#### Discussion

Real-world light sources often measure color of illumination based on a black-body temperature scale. For example, the colors and characterizations of typical home and office light fixtures correspond to the following temperatures:

| Label | Color | Temperature |
| --- | --- | --- |
| “Soft white” | Warm, yellowish white | 2700 K |
| “Bright white” | Pale yellowish white | 3000 K |
| “Daylight” | Bright, slightly greenish white | 5000 K |
| “Cool daylight” | Bright, slightly bluish white | 6500 K |

## Parameters

- `temperature`: The black-body temperature, in Kelvins, whose luminous color the light should match.

## See Also

- [var color: CGColor?](mdlphysicallyplausiblelight/color.md)
  The color of the light source.
- [var lumens: Float](mdlphysicallyplausiblelight/lumens.md)
  The total visible intensity of the light source, in lumens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight/setcolorbytemperature(_:))*