# deviceBrowser(_:didRemove:moreGoing:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) deviceBrowser:(ICDeviceBrowser *) browser didRemoveDevice:(ICDevice *) device moreGoing:(BOOL) moreGoing;
```

## Discussion

If several devices are removed at the same time, then this message is sent once for each device with the value of `moreGoing` set to `true` in each message except the last one.

## See Also

### Adding and Removing Devices
- [func deviceBrowser(ICDeviceBrowser, didAdd: ICDevice, moreComing: Bool)](./devicebrowser%28_,didadd,morecoming%29.md)
  Tells the delegate that a device has been added.
- [func deviceBrowserDidEnumerateLocalDevices(ICDeviceBrowser)](./devicebrowserdidenumeratelocaldevices%28_%29.md)
  Tells the delegate that the device browser has completed sending [`deviceBrowser(_:didAdd:moreComing:)`](./devicebrowser%28_,didadd,morecoming%29.md) for all local devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowserdelegate/devicebrowser(_:didremove:moregoing:))*