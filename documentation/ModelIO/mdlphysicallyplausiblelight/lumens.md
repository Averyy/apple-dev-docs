# lumens

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The total visible intensity of the light source, in lumens.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lumens: Float { get set }
```

```objc
@property (nonatomic, readwrite) float lumens;
```

## Discussion

The default intensity is 1000 lumens.

## See Also

### Managing Light Color and Intensity
- [var color: CGColor?](./color.md)
  The color of the light source.
- [func setColorByTemperature(Float)](./setcolorbytemperature%28_%29.md)
  Sets the light’s color based on a black-body temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight/lumens)*