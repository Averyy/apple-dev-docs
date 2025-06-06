# didRemove(_:)

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
func didRemove(_ device: ICDevice)
```

## See Also

- [func device(ICDevice, didOpenSessionWithError: (any Error)?)](icdevicedelegate/device(_:didopensessionwitherror:).md)
  Tells the delegate when a session is opened on a device.
- [func device(ICDevice, didCloseSessionWithError: (any Error)?)](icdevicedelegate/device(_:didclosesessionwitherror:).md)
  Tells the delegate when a session is closed on a device.
- [func deviceDidBecomeReady(ICDevice)](icdevicedelegate/devicedidbecomeready(_:).md)
  Tells the delegate when the device is ready to receive requests.
- [func device(ICDevice, didReceiveStatusInformation: [ICDeviceStatus : Any])](icdevicedelegate/device(_:didreceivestatusinformation:).md)
  Tells the delegate when status information is received from a device.
- [func device(ICDevice, didEncounterError: (any Error)?)](icdevicedelegate/device(_:didencountererror:).md)
  Tells the delegate when a device encounters an error.
- [func device(ICDevice, didEjectWithError: (any Error)?)](icdevicedelegate/device(_:didejectwitherror:).md)
  Tells the delegate when the ejection is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate/didremove(_:))*