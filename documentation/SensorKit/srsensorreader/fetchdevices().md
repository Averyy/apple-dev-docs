# fetchDevices()

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Acquires device information for all devices that store data for this reader’s sensor.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
func fetchDevices()
```

```objc
- (void) fetchDevices;
```

#### Discussion

Upon success, the framework provides an array of devices to the delegate via [`sensorReader(_:didFetch:)`](../srsensorreaderdelegate/sensorreader%28_,didfetch%29.md). Upon failure, the framework invokes the delegate’s [`sensorReader(_:fetchDevicesDidFailWithError:)`](../srsensorreaderdelegate/sensorreader%28_,fetchdevicesdidfailwitherror%29.md) callback.

## See Also

### Reading recorded data
- [func fetch(SRFetchRequest)](./fetch%28_%29.md)
  Fetches the samples that a fetch request specifies.
- [class SRDevice](../srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetchdevices())*