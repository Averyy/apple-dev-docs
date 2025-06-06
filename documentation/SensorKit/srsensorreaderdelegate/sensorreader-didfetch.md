# sensorReader(_:didFetch:)

**Framework**: SensorKit  
**Kind**: method

Provides the delegate with one or more devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, didFetch devices: [SRDevice])
```

## Parameters

- `reader`: The sensor reader that fetched the device(s).
- `devices`: The fetched devices.

## See Also

- [func sensorReader(SRSensorReader, fetchDevicesDidFailWithError: any Error)](srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:).md)
  Provides the delegate a reason when the reader fails to fetch devices.
- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:))*