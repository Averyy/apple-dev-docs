# devices

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

All devices found by the browser.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var devices: [ICDevice]? { get }
```

```objc
@property (readonly, nullable) NSArray<ICDevice *> * devices;
```

## Discussion

This array is empty before the first invocation of the delegate method [`deviceBrowser(_:didAdd:moreComing:)`](../icdevicebrowserdelegate/devicebrowser%28_,didadd,morecoming%29.md). The value of this property changes as devices appear and disappear.

## See Also

### Browsing Devices
- [var isBrowsing: Bool](./isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [class ICDevice](../icdevice.md)
  An abstract object that represents a device.
- [var browsedDeviceTypeMask: ICDeviceTypeMask](./browseddevicetypemask.md)
  A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.
- [func start()](./start%28%29.md)
  Tells the delegate to start looking for devices.
- [func stop()](./stop%28%29.md)
  Tells the delegate to stop looking for devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/devices)*