# requestOpenSession(options:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Requests to open a session on the device, then executes the completion handler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestOpenSession(options: [ICSessionOptions : Any]? = nil, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func requestOpenSession(options: [ICSessionOptions : Any]? = nil) async throws
```

```objc
- (void) requestOpenSessionWithOptions:(NSDictionary<NSString *,id> *) options completion:(void (^)(NSError *error)) completion;
```

## Discussion

Execution of the completion block occurs on the calling thread.

## See Also

### Managing a Device
- [var delegate: (any ICDeviceDelegate)?](./delegate.md)
  The delegate to receive messages once a session is opened on the device.
- [protocol ICDeviceDelegate](../icdevicedelegate.md)
  Methods for responding to device events and changes.
- [var hasOpenSession: Bool](./hasopensession.md)
  A Boolean value that indicates whether the device has an open session.
- [func requestOpenSession()](./requestopensession%28%29.md)
  Requests to open a session on the device.
- [func requestSendMessage(UInt32, outData: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](./requestsendmessage%28_,outdata,maxreturneddatasize,sendmessagedelegate,didsendmessageselector,contextinfo%29.md)
  Asynchronously sends an arbitrary message with optional data to a device.
- [func requestCloseSession()](./requestclosesession%28%29.md)
  Requests to close an open session on the device.
- [func requestCloseSession(options: [ICSessionOptions : Any]?, completion: ((any Error)?) -> Void)](./requestclosesession%28options,completion%29.md)
  Requests to close an open session on the device, then executes the completion handler.
- [func requestEject()](./requesteject%28%29.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestEject(completion: ((any Error)?) -> Void)](./requesteject%28completion%29.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device, then executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/requestopensession(options:completion:))*