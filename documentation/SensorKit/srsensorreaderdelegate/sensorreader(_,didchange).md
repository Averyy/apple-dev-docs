# sensorReader(_:didChange:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate of the reader’s new authorization status.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, didChange authorizationStatus: SRAuthorizationStatus)
```

```objc
- (void) sensorReader:(SRSensorReader *) reader didChangeAuthorizationStatus:(SRAuthorizationStatus) authorizationStatus;
```

## Parameters

- `reader`: The sensor reader whose authorization state changed.
- `authorizationStatus`: A flag indicating whether the framework authorizes the sensor reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:))*