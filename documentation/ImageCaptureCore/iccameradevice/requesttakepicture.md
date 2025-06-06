# requestTakePicture()

**Framework**: ImageCaptureCore  
**Kind**: method

Captures a new image using the camera.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestTakePicture()
```

#### Discussion

Before taking a picture, you must first enable tethering by calling [`requestEnableTethering()`](iccameradevice/requestenabletethering().md).

## See Also

- [var tetheredCaptureEnabled: Bool](iccameradevice/tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
- [var ptpEventHandler: (Data) -> Void](iccameradevice/ptpeventhandler.md)
  A closure for handling PTP event packets.
- [func requestEnableTethering()](iccameradevice/requestenabletethering.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestSendPTPCommand(Data, outData: Data?, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestsendptpcommand(_:outdata:sendcommanddelegate:didsendcommand:contextinfo:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestSendPTPCommand(Data, outData: Data?, completion: (Data, Data, (any Error)?) -> Void)](iccameradevice/requestsendptpcommand(_:outdata:completion:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](iccameradevice/requestdisabletethering.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requesttakepicture())*