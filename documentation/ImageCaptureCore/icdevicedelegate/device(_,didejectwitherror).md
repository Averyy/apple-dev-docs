# device(_:didEjectWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) device:(ICDevice *) device didEjectWithError:(NSError *) error;
```

## Discussion

Execution of the delegate callback occurs on the main thread.

## See Also

### Responding to Device Events
- [func device(ICDevice, didOpenSessionWithError: (any Error)?)](./device%28_,didopensessionwitherror%29.md)
  Tells the delegate when a session is opened on a device.
- [func device(ICDevice, didCloseSessionWithError: (any Error)?)](./device%28_,didclosesessionwitherror%29.md)
  Tells the delegate when a session is closed on a device.
- [func didRemove(ICDevice)](./didremove%28_%29.md)
  Tells the delegate that a device has been removed.
- [func deviceDidBecomeReady(ICDevice)](./devicedidbecomeready%28_%29.md)
  Tells the delegate when the device is ready to receive requests.
- [func device(ICDevice, didReceiveStatusInformation: [ICDeviceStatus : Any])](./device%28_,didreceivestatusinformation%29.md)
  Tells the delegate when status information is received from a device.
- [func device(ICDevice, didEncounterError: (any Error)?)](./device%28_,didencountererror%29.md)
  Tells the delegate when a device encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate/device(_:didejectwitherror:))*