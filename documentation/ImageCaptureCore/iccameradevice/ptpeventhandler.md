# ptpEventHandler

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A closure for handling PTP event packets.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var ptpEventHandler: (Data) -> Void { get set }
```

```objc
@property (nonatomic, copy) void (^ptpEventHandler)(NSData *eventData);
```

#### Discussion

Set this property as an alternative to setting up an object to handle PTP event packets. If the handler is set, it is called in place of the [`delegate`](../icdevice/delegate.md). If the handler is `nil`, the [`delegate`](../icdevice/delegate.md) is called, if present. If both are set, only the handler is called.

## See Also

### Taking Pictures
- [var tetheredCaptureEnabled: Bool](./tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
- [func requestEnableTethering()](./requestenabletethering%28%29.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestTakePicture()](./requesttakepicture%28%29.md)
  Captures a new image using the camera.
- [func requestSendPTPCommand(Data, outData: Data?, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)](./requestsendptpcommand%28_,outdata,sendcommanddelegate,didsendcommand,contextinfo%29.md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestSendPTPCommand(Data, outData: Data?, completion: (Data, Data, (any Error)?) -> Void)](./requestsendptpcommand%28_,outdata,completion%29.md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](./requestdisabletethering%28%29.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/ptpeventhandler)*