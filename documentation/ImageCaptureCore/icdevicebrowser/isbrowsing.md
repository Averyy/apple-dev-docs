# isBrowsing

**Framework**: ImageCaptureCore  
**Kind**: property

A Boolean value indicating whether the device browser is browsing for devices.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var isBrowsing: Bool { get }
```

## See Also

- [var devices: [ICDevice]?](icdevicebrowser/devices.md)
  All devices found by the browser.
- [class ICDevice](icdevice.md)
  An abstract object that represents a device.
- [var browsedDeviceTypeMask: ICDeviceTypeMask](icdevicebrowser/browseddevicetypemask.md)
  A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.
- [func start()](icdevicebrowser/start.md)
  Tells the delegate to start looking for devices.
- [func stop()](icdevicebrowser/stop.md)
  Tells the delegate to stop looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/isbrowsing)*