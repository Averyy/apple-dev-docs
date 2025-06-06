# preferredDevice

**Framework**: ImageCaptureCore  
**Kind**: property

Returns a device object that the client application should select when it launches.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var preferredDevice: ICDevice? { get }
```

#### Discussion

If the client application that calls this method is the autolaunch application associated with a device, and that device is the last one attached (through USB, FireWire, or network), then that device is the preferred device.

Call this method in the implementation of [`deviceBrowser(_:didAdd:moreComing:)`](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md) if the value of `moreComing` is `false`; or in the implementation of [`deviceBrowserDidEnumerateLocalDevices(_:)`](icdevicebrowserdelegate/devicebrowserdidenumeratelocaldevices(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/preferreddevice)*