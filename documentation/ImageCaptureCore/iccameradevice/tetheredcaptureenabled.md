# tetheredCaptureEnabled

**Framework**: ImageCaptureCore  
**Kind**: property

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

#### Discussion

Use [`requestEnableTethering()`](iccameradevice/requestenabletethering().md) and [`requestDisableTethering()`](iccameradevice/requestdisabletethering().md) to enable or disable tethered capture.

## See Also

- [var ptpEventHandler: (Data) -> Void](iccameradevice/ptpeventhandler.md)
  A closure for handling PTP event packets.
- [func requestEnableTethering()](iccameradevice/requestenabletethering.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestTakePicture()](iccameradevice/requesttakepicture.md)
  Captures a new image using the camera.
- [func requestSendPTPCommand(Data, outData: Data?, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestsendptpcommand(_:outdata:sendcommanddelegate:didsendcommand:contextinfo:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestSendPTPCommand(Data, outData: Data?, completion: (Data, Data, (any Error)?) -> Void)](iccameradevice/requestsendptpcommand(_:outdata:completion:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](iccameradevice/requestdisabletethering.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/tetheredcaptureenabled)*