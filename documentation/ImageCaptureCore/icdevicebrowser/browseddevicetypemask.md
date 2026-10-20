# browsedDeviceTypeMask

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readwrite) ICDeviceTypeMask browsedDeviceTypeMask;
```

#### Discussion

Construct this property by performing bitwise OR on values of [`ICDeviceTypeMask`](../icdevicetypemask.md) with values of [`ICDeviceLocationTypeMask`](../icdevicelocationtypemask.md). You can change this property while the browser is looking for devices.

## See Also

### Browsing Devices
- [var isBrowsing: Bool](./isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [var devices: [ICDevice]?](./devices.md)
  All devices found by the browser.
- [class ICDevice](../icdevice.md)
  An abstract object that represents a device.
- [func start()](./start%28%29.md)
  Tells the delegate to start looking for devices.
- [func stop()](./stop%28%29.md)
  Tells the delegate to stop looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/browseddevicetypemask)*