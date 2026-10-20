# sensor

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The particular sensor that this object reads.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
var sensor: SRSensor { get }
```

```objc
@property (copy, readonly) SRSensor sensor;
```

#### Discussion

The framework sets this property to the sensor you pass into [`init(sensor:)`](./init%28sensor%29.md).

## See Also

### Creating a sensor reader
- [init(sensor: SRSensor)](./init%28sensor%29.md)
  Initializes a new sensor reader object.
- [struct SRSensor](../srsensor.md)
  The sensors an app can read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/sensor)*