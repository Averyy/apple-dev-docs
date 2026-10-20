# requestSendPTPCommand(_:outData:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method

Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestSendPTPCommand(_ ptpCommand: Data, outData ptpData: Data?) async throws -> (Data, Data)
```

#### Discussion

The block receives the response, data, and an error message, if present.

## See Also

- [var tetheredCaptureEnabled: Bool](iccameradevice/tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
- [var ptpEventHandler: (Data) -> Void](iccameradevice/ptpeventhandler.md)
  A closure for handling PTP event packets.
- [func requestEnableTethering()](iccameradevice/requestenabletethering.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestTakePicture()](iccameradevice/requesttakepicture.md)
  Captures a new image using the camera.
- [func requestSendPTPCommand(Data, outData: Data?, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)](iccameradevice/requestsendptpcommand(_:outdata:sendcommanddelegate:didsendcommand:contextinfo:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](iccameradevice/requestdisabletethering.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestsendptpcommand(_:outdata:completion:))*