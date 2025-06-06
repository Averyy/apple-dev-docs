# deviceBrowser(_:didRemove:moreGoing:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the delegate that a device has been removed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func deviceBrowser(_ browser: ICDeviceBrowser, didRemove device: ICDevice, moreGoing: Bool)
```

#### Discussion

If several devices are removed at the same time, then this message is sent once for each device with the value of `moreGoing` set to `true` in each message except the last one.

## See Also

- [func deviceBrowser(ICDeviceBrowser, didAdd: ICDevice, moreComing: Bool)](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md)
  Tells the delegate that a device has been added.
- [func deviceBrowserDidEnumerateLocalDevices(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserdidenumeratelocaldevices(_:).md)
  Tells the delegate that the device browser has completed sending [`deviceBrowser(_:didAdd:moreComing:)`](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md) for all local devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate/devicebrowser(_:didremove:moregoing:))*