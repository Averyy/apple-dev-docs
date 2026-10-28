# tetheredCaptureEnabled

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether tethered capture is enabled on the camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var tetheredCaptureEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL tetheredCaptureEnabled;
```

## Discussion

Use [`requestEnableTethering()`](./requestenabletethering%28%29.md) and [`requestDisableTethering()`](./requestdisabletethering%28%29.md) to enable or disable tethered capture.

## See Also

### Taking Pictures
- [var ptpEventHandler: (Data) -> Void](./ptpeventhandler.md)
  A closure for handling PTP event packets.
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

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/tetheredcaptureenabled)*