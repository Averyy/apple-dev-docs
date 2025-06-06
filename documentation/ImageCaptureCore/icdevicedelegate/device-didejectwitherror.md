# device(_:didEjectWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the delegate when the ejection is complete.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
optional func device(_ device: ICDevice, didEjectWithError error: (any Error)?)
```

#### Discussion

Execution of the delegate callback occurs on the main thread.

## See Also

- [func device(ICDevice, didOpenSessionWithError: (any Error)?)](icdevicedelegate/device(_:didopensessionwitherror:).md)
  Tells the delegate when a session is opened on a device.
- [func device(ICDevice, didCloseSessionWithError: (any Error)?)](icdevicedelegate/device(_:didclosesessionwitherror:).md)
  Tells the delegate when a session is closed on a device.
- [func didRemove(ICDevice)](icdevicedelegate/didremove(_:).md)
  Tells the delegate that a device has been removed.
- [func deviceDidBecomeReady(ICDevice)](icdevicedelegate/devicedidbecomeready(_:).md)
  Tells the delegate when the device is ready to receive requests.
- [func device(ICDevice, didReceiveStatusInformation: [ICDeviceStatus : Any])](icdevicedelegate/device(_:didreceivestatusinformation:).md)
  Tells the delegate when status information is received from a device.
- [func device(ICDevice, didEncounterError: (any Error)?)](icdevicedelegate/device(_:didencountererror:).md)
  Tells the delegate when a device encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate/device(_:didejectwitherror:))*