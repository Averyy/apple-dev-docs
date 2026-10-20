# requestCloseSession()

**Framework**: ImageCaptureCore  
**Kind**: method

Requests to close an open session on the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func requestCloseSession()
```

#### Discussion

Once the request to close the session has completed, [`device(_:didCloseSessionWithError:)`](icdevicedelegate/device(_:didclosesessionwitherror:).md) is called on the delegate.

Execution of the delegate callback occurs on the main thread.

## See Also

- [var delegate: (any ICDeviceDelegate)?](icdevice/delegate.md)
  The delegate to receive messages once a session is opened on the device.
- [protocol ICDeviceDelegate](icdevicedelegate.md)
  Methods for responding to device events and changes.
- [var hasOpenSession: Bool](icdevice/hasopensession.md)
  A Boolean value that indicates whether the device has an open session.
- [func requestOpenSession()](icdevice/requestopensession.md)
  Requests to open a session on the device.
- [func requestOpenSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestopensession(options:completion:).md)
  Requests to open a session on the device, then executes the completion handler.
- [func requestSendMessage(UInt32, outData: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](icdevice/requestsendmessage(_:outdata:maxreturneddatasize:sendmessagedelegate:didsendmessageselector:contextinfo:).md)
  Asynchronously sends an arbitrary message with optional data to a device.
- [func requestCloseSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestclosesession(options:completion:).md)
  Requests to close an open session on the device, then executes the completion handler.
- [func requestEject()](icdevice/requesteject.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestEject(completion: ((any Error)?) -> Void)](icdevice/requesteject(completion:).md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device, then executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/requestclosesession())*