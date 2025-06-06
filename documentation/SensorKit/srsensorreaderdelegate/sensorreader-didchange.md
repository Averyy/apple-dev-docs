# sensorReader(_:didChange:)

**Framework**: SensorKit  
**Kind**: method

Notifies the delegate of the reader’s new authorization status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, didChange authorizationStatus: SRAuthorizationStatus)
```

## Parameters

- `reader`: The sensor reader whose authorization state changed.
- `authorizationStatus`: A flag indicating whether the framework authorizes the sensor reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didchange:))*