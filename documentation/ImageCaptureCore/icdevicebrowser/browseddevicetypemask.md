# browsedDeviceTypeMask

**Framework**: ImageCaptureCore  
**Kind**: property

A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var browsedDeviceTypeMask: ICDeviceTypeMask { get set }
```

#### Discussion

Construct this property by performing bitwise OR on values of [`ICDeviceTypeMask`](icdevicetypemask.md) with values of [`ICDeviceLocationTypeMask`](icdevicelocationtypemask.md). You can change this property while the browser is looking for devices.

## See Also

- [var isBrowsing: Bool](icdevicebrowser/isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [var devices: [ICDevice]?](icdevicebrowser/devices.md)
  All devices found by the browser.
- [class ICDevice](icdevice.md)
  An abstract object that represents a device.
- [func start()](icdevicebrowser/start.md)
  Tells the delegate to start looking for devices.
- [func stop()](icdevicebrowser/stop.md)
  Tells the delegate to stop looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/browseddevicetypemask)*