# temperatureUncertainty

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The amount of uncertainty in the measurement of the water temperature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var temperatureUncertainty: Measurement<UnitTemperature> { get }
```

```objc
@property (nonatomic, readonly) NSMeasurement<NSUnitTemperature *> * temperatureUncertainty;
```

## See Also

### Accessing the data
- [var date: Date](./date.md)
  The time and date when the system recorded the measurements.
- [var temperature: Measurement<UnitTemperature>](./temperature.md)
  The water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatertemperature/temperatureuncertainty)*