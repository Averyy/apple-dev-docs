# fetchDevices()

**Framework**: SensorKit  
**Kind**: method

Acquires device information for all devices that store data for this reader’s sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func fetchDevices()
```

#### Discussion

Upon success, the framework provides an array of devices to the delegate via [`sensorReader(_:didFetch:)`](srsensorreaderdelegate/sensorreader(_:didfetch:).md). Upon failure, the framework invokes the delegate’s [`sensorReader(_:fetchDevicesDidFailWithError:)`](srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:).md) callback.

## See Also

- [func fetch(SRFetchRequest)](srsensorreader/fetch(_:).md)
  Fetches the samples that a fetch request specifies.
- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())*