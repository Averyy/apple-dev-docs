# sensorReader(_:didFetch:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the delegate with one or more devices.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, didFetch devices: [SRDevice])
```

```objc
- (void) sensorReader:(SRSensorReader *) reader didFetchDevices:(NSArray<SRDevice *> *) devices;
```

## Parameters

- `reader`: The sensor reader that fetched the device(s).
- `devices`: The fetched devices.

## See Also

### Fetching Devices
- [func sensorReader(SRSensorReader, fetchDevicesDidFailWithError: any Error)](./sensorreader%28_,fetchdevicesdidfailwitherror%29.md)
  Provides the delegate a reason when the reader fails to fetch devices.
- [class SRDevice](../srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didfetch:))*