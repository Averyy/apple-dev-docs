# init(sensor:)

**Framework**: SensorKit  
**Kind**: init  
**Role**: Initializer

Initializes a new sensor reader object.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
init(sensor: SRSensor)
```

```objc
- (instancetype) initWithSensor:(SRSensor) sensor;
```

## Parameters

- `sensor`: The sensor from which to read information.

## See Also

### Creating a sensor reader
- [struct SRSensor](../srsensor.md)
  The sensors an app can read.
- [var sensor: SRSensor](./sensor.md)
  The particular sensor that this object reads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/init(sensor:))*