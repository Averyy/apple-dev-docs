# requestDisableTethering()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Disables tethered capture on the camera.

**Availability**:
- macOS 10.4+ - Deprecated in 14.0

> **Deprecated**: Third party cameras that support the standard take picture command will have the capability enabled by default. This call will have no effect

## Declaration

```swift
func requestDisableTethering()
```

```objc
- (void) requestDisableTethering;
```

## See Also

### Taking Pictures
- [var tetheredCaptureEnabled: Bool](./tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestdisabletethering())*