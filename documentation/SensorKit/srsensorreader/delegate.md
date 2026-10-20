# delegate

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

An object that responds to sensor-related events.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
weak var delegate: (any SRSensorReaderDelegate)? { get set }
```

```objc
@property (weak) id<SRSensorReaderDelegate> delegate;
```

## See Also

### Responding to sensor events
- [protocol SRSensorReaderDelegate](../srsensorreaderdelegate.md)
  A set of callbacks the framework invokes to notify the app of sensor-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/delegate)*