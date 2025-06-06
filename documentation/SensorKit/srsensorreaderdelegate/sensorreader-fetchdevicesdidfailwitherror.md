# sensorReader(_:fetchDevicesDidFailWithError:)

**Framework**: SensorKit  
**Kind**: method

Provides the delegate a reason when the reader fails to fetch devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, fetchDevicesDidFailWithError error: any Error)
```

## Parameters

- `reader`: The reader that failed to fetch devices.
- `error`: An object that describes the cause of failure.

## See Also

- [func sensorReader(SRSensorReader, didFetch: [SRDevice])](srsensorreaderdelegate/sensorreader(_:didfetch:).md)
  Provides the delegate with one or more devices.
- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:))*