# stop()

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the delegate to stop looking for devices.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

#### Discussion

Calling this method frees all device instances that are not in use.

## See Also

- [var isBrowsing: Bool](icdevicebrowser/isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [var devices: [ICDevice]?](icdevicebrowser/devices.md)
  All devices found by the browser.
- [class ICDevice](icdevice.md)
  An abstract object that represents a device.
- [var browsedDeviceTypeMask: ICDeviceTypeMask](icdevicebrowser/browseddevicetypemask.md)
  A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.
- [func start()](icdevicebrowser/start.md)
  Tells the delegate to start looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/stop())*