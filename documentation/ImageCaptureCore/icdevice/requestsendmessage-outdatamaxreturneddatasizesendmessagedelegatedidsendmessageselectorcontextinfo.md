# requestSendMessage(_:outData:maxReturnedDataSize:sendMessageDelegate:didSendMessageSelector:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Asynchronously sends an arbitrary message with optional data to a device.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestSendMessage(_ messageCode: UInt32, outData data: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector selector: Selector, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Use this method to send a private message from a client application to a device module.

The `sendMessageDelegate` must implement a function with the signature `(void)didSendMessage:(UInt32)messageCode inData:(NSData*)data error:(NSError*)error contextInfo:(void*)contextInfo`, to be called when the request is completed.

Do not use this method to send PTP pass-through commands to a PTP camera. Use [`requestSendPTPCommand(_:outData:sendCommandDelegate:didSendCommand:contextInfo:)`](iccameradevice/requestsendptpcommand(_:outdata:sendcommanddelegate:didsendcommand:contextinfo:).md) instead.

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
- [func requestCloseSession()](icdevice/requestclosesession.md)
  Requests to close an open session on the device.
- [func requestCloseSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](icdevice/requestclosesession(options:completion:).md)
  Requests to close an open session on the device, then executes the completion handler.
- [func requestEject()](icdevice/requesteject.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestEject(completion: ((any Error)?) -> Void)](icdevice/requesteject(completion:).md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device, then executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/requestsendmessage(_:outdata:maxreturneddatasize:sendmessagedelegate:didsendmessageselector:contextinfo:))*