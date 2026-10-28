# device

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The device to query for sample data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var device: SRDevice { get set }
```

```objc
@property (strong) SRDevice * device;
```

## Discussion

If the app doesn’t define a value for this property, the framework queries the current device. To get a list of available devices, the app calls [`fetchDevices()`](../srsensorreader/fetchdevices%28%29.md) on its sensor reader.

## See Also

### Selecting the Device
- [class SRDevice](../srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchrequest/device)*