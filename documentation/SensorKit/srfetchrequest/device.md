# device

**Framework**: SensorKit  
**Kind**: property

The device to query for sample data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var device: SRDevice { get set }
```

#### Discussion

If the app doesn’t define a value for this property, the framework queries the current device. To get a list of available devices, the app calls [`fetchDevices()`](srsensorreader/fetchdevices().md) on its sensor reader.

## See Also

- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device)*