# requestTakePicture()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Captures a new image using the camera.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestTakePicture()
```

```objc
- (void) requestTakePicture;
```

#### Discussion

Before taking a picture, you must first enable tethering by calling [`requestEnableTethering()`](./requestenabletethering%28%29.md).

## See Also

### Taking Pictures
- [var tetheredCaptureEnabled: Bool](./tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
- [var ptpEventHandler: (Data) -> Void](./ptpeventhandler.md)
  A closure for handling PTP event packets.
- [func requestEnableTethering()](./requestenabletethering%28%29.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestSendPTPCommand(Data, outData: Data?, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)](./requestsendptpcommand%28_,outdata,sendcommanddelegate,didsendcommand,contextinfo%29.md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestSendPTPCommand(Data, outData: Data?, completion: (Data, Data, (any Error)?) -> Void)](./requestsendptpcommand%28_,outdata,completion%29.md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](./requestdisabletethering%28%29.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requesttakepicture())*