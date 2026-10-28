# ICDeviceDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol  
**Role**: Protocol

Methods for responding to device events and changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
protocol ICDeviceDelegate : NSObjectProtocol
```

```objc
@protocol ICDeviceDelegate <NSObject>
```

## Overview

Unless otherwise noted, all completion blocks execute on the calling thread.

## Topics

### Responding to Device Events
- [func device(ICDevice, didOpenSessionWithError: (any Error)?)](./icdevicedelegate/device%28_,didopensessionwitherror%29.md)
  Tells the delegate when a session is opened on a device.
- [func device(ICDevice, didCloseSessionWithError: (any Error)?)](./icdevicedelegate/device%28_,didclosesessionwitherror%29.md)
  Tells the delegate when a session is closed on a device.
- [func didRemove(ICDevice)](./icdevicedelegate/didremove%28_%29.md)
  Tells the delegate that a device has been removed.
- [func deviceDidBecomeReady(ICDevice)](./icdevicedelegate/devicedidbecomeready%28_%29.md)
  Tells the delegate when the device is ready to receive requests.
- [func device(ICDevice, didReceiveStatusInformation: [ICDeviceStatus : Any])](./icdevicedelegate/device%28_,didreceivestatusinformation%29.md)
  Tells the delegate when status information is received from a device.
- [func device(ICDevice, didEncounterError: (any Error)?)](./icdevicedelegate/device%28_,didencountererror%29.md)
  Tells the delegate when a device encounters an error.
- [func device(ICDevice, didEjectWithError: (any Error)?)](./icdevicedelegate/device%28_,didejectwitherror%29.md)
  Tells the delegate when the ejection is complete.
### Responding to Device Changes
- [func deviceDidChangeName(ICDevice)](./icdevicedelegate/devicedidchangename%28_%29.md)
  Tells the delegate when the name of a device changes.
- [func deviceDidChangeSharingState(ICDevice)](./icdevicedelegate/devicedidchangesharingstate%28_%29.md)
  Tells the delegate when the sharing state of a device changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [ICCameraDeviceDelegate](./iccameradevicedelegate.md)
- [ICScannerDeviceDelegate](./icscannerdevicedelegate.md)

## See Also

### Managing a Device
- [var delegate: (any ICDeviceDelegate)?](./icdevice/delegate.md)
  The delegate to receive messages once a session is opened on the device.
- [var hasOpenSession: Bool](./icdevice/hasopensession.md)
  A Boolean value that indicates whether the device has an open session.
- [func requestOpenSession()](./icdevice/requestopensession%28%29.md)
  Requests to open a session on the device.
- [func requestOpenSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](./icdevice/requestopensession%28options,completion%29.md)
  Requests to open a session on the device, then executes the completion handler.
- [func requestSendMessage(UInt32, outData: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](./icdevice/requestsendmessage%28_,outdata,maxreturneddatasize,sendmessagedelegate,didsendmessageselector,contextinfo%29.md)
  Asynchronously sends an arbitrary message with optional data to a device.
- [func requestCloseSession()](./icdevice/requestclosesession%28%29.md)
  Requests to close an open session on the device.
- [func requestCloseSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](./icdevice/requestclosesession%28options,completion%29.md)
  Requests to close an open session on the device, then executes the completion handler.
- [func requestEject()](./icdevice/requesteject%28%29.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestEject(completion: ((any Error)?) -> Void)](./icdevice/requesteject%28completion%29.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device, then executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate)*