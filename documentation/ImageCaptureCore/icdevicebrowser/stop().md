# stop()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) stop;
```

## Discussion

Calling this method frees all device instances that are not in use.

## See Also

### Browsing Devices
- [var isBrowsing: Bool](./isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [var devices: [ICDevice]?](./devices.md)
  All devices found by the browser.
- [class ICDevice](../icdevice.md)
  An abstract object that represents a device.
- [var browsedDeviceTypeMask: ICDeviceTypeMask](./browseddevicetypemask.md)
  A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.
- [func start()](./start%28%29.md)
  Tells the delegate to start looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/stop())*