# color

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, nullable) CGColorRef color;
```

#### Discussion

The default color corresponds to a color temperature of 6500 K, as described by the [`setColorByTemperature(_:)`](./setcolorbytemperature%28_%29.md) method.

## See Also

### Managing Light Color and Intensity
- [var lumens: Float](./lumens.md)
  The total visible intensity of the light source, in lumens.
- [func setColorByTemperature(Float)](./setcolorbytemperature%28_%29.md)
  Sets the light’s color based on a black-body temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight/color)*