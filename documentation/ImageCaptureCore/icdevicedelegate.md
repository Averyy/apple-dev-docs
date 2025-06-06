# ICDeviceDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol

Methods for responding to device events and changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
protocol ICDeviceDelegate : NSObjectProtocol
```

#### Overview

Unless otherwise noted, all completion blocks execute on the calling thread.

## Topics

### Responding to Device Events
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
- [func device(ICDevice, didEjectWithError: (any Error)?)](icdevicedelegate/device(_:didejectwitherror:).md)
  Tells the delegate when the ejection is complete.
### Responding to Device Changes
- [func deviceDidChangeName(ICDevice)](icdevicedelegate/devicedidchangename(_:).md)
  Tells the delegate when the name of a device changes.
- [func deviceDidChangeSharingState(ICDevice)](icdevicedelegate/devicedidchangesharingstate(_:).md)
  Tells the delegate when the sharing state of a device changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [ICCameraDeviceDelegate](iccameradevicedelegate.md)
- [ICScannerDeviceDelegate](icscannerdevicedelegate.md)

## See Also

- [var delegate: (any ICDeviceDelegate)?](icdevice/delegate.md)
  The delegate to receive messages once a session is opened on the device.
- [var hasOpenSession: Bool](icdevice/hasopensession.md)
  A Boolean value that indicates whether the device has an open session.
- [func requestOpenSession()](icdevice/requestopensession.md)
  Requests to open a session on the device.
- [func requestOpenSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestopensession(options:completion:).md)
  Requests to open a session on the device, then executes the completion handler.
- [func requestSendMessage(UInt32, outData: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](icdevice/requestsendmessage(_:outdata:maxreturneddatasize:sendmessagedelegate:didsendmessageselector:contextinfo:).md)
  Asynchronously sends an arbitrary message with optional data to a device.
- [func requestCloseSession()](icdevice/requestclosesession.md)
  Requests to close an open session on the device.
- [func requestCloseSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestclosesession(options:completion:).md)
  Requests to close an open session on the device, then executes the completion handler.
- [func requestEject()](icdevice/requesteject.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestEject(completion: ((any Error)?) -> Void)](icdevice/requesteject(completion:).md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device, then executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate)*