# errorEstimate

**Framework**: SensorKit  
**Kind**: property

An estimate of the amount of error in the temperature measurement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var errorEstimate: Measurement<UnitTemperature> { get }
```

#### Discussion

This property is a delta value that can be positive or negative.

## See Also

- [var timestamp: Date](srwristtemperature/timestamp.md)
  The date and time when the device records the temperature.
- [var value: Measurement<UnitTemperature>](srwristtemperature/value.md)
  The temperature sensor value in celsius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristtemperature/errorestimate)*