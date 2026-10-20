# timestamp

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The date and time when the device records the temperature.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var timestamp: Date { get }
```

```objc
@property (nonatomic, strong, readonly) NSDate * timestamp;
```

## See Also

### Getting temperature information
- [var value: Measurement<UnitTemperature>](./value.md)
  The temperature sensor value in celsius.
- [var errorEstimate: Measurement<UnitTemperature>](./errorestimate.md)
  An estimate of the amount of error in the temperature measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristtemperature/timestamp)*