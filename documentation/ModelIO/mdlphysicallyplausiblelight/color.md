# color

**Framework**: Model I/O  
**Kind**: property

The color of the light source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var color: CGColor? { get set }
```

#### Discussion

The default color corresponds to a color temperature of 6500 K, as described by the [`setColorByTemperature(_:)`](mdlphysicallyplausiblelight/setcolorbytemperature(_:).md) method.

## See Also

- [var lumens: Float](mdlphysicallyplausiblelight/lumens.md)
  The total visible intensity of the light source, in lumens.
- [func setColorByTemperature(Float)](mdlphysicallyplausiblelight/setcolorbytemperature(_:).md)
  Sets the light’s color based on a black-body temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight/color)*