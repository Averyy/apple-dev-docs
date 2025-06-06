# deviceBrowser(_:didAdd:moreComing:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Required**: Yes

Tells the delegate that a device has been added.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func deviceBrowser(_ browser: ICDeviceBrowser, didAdd device: ICDevice, moreComing: Bool)
```

#### Discussion

If several devices are found during the initial search, then this message is sent once for each device with the value of `moreComing` set to `true` in each message except the last one.

Not all devices are reported using this method. Devices that fail to communicate successfully are silently ignored.

## See Also

- [func deviceBrowser(ICDeviceBrowser, didRemove: ICDevice, moreGoing: Bool)](icdevicebrowserdelegate/devicebrowser(_:didremove:moregoing:).md)
  Tells the delegate that a device has been removed.
- [func deviceBrowserDidEnumerateLocalDevices(ICDeviceBrowser)](icdevicebrowserdelegate/devicebrowserdidenumeratelocaldevices(_:).md)
  Tells the delegate that the device browser has completed sending [`deviceBrowser(_:didAdd:moreComing:)`](icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:).md) for all local devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate/devicebrowser(_:didadd:morecoming:))*