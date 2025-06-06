# requestSendPTPCommand(_:outData:sendCommandDelegate:didSendCommand:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func requestSendPTPCommand(_ command: Data, outData data: Data?, sendCommandDelegate: Any, didSendCommand selector: Selector, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Call this method only if the [`capabilities`](icdevice/capabilities.md) property contains [`cameraDeviceCanAcceptPTPCommands`](icdevicecapability/cameradevicecanacceptptpcommands.md). All PTP cameras have this capability.

The `sendCommandDelegate` must implement a function with the signature `- (void)didSendPTPCommand:(NSData*)command inData:(NSData*)data response:(NSData*)response error:(NSError*)error contextInfo:(void*)contextInfo`, to be called when the request is completed.

## See Also

- [var tetheredCaptureEnabled: Bool](iccameradevice/tetheredcaptureenabled.md)
  A Boolean value indicating whether tethered capture is enabled on the camera.
- [var ptpEventHandler: (Data) -> Void](iccameradevice/ptpeventhandler.md)
  A closure for handling PTP event packets.
- [func requestEnableTethering()](iccameradevice/requestenabletethering.md)
  Enables tethered capture if the camera has the capability to take pictures while connected.
- [func requestTakePicture()](iccameradevice/requesttakepicture.md)
  Captures a new image using the camera.
- [func requestSendPTPCommand(Data, outData: Data?, completion: (Data, Data, (any Error)?) -> Void)](iccameradevice/requestsendptpcommand(_:outdata:completion:).md)
  Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.
- [func requestDisableTethering()](iccameradevice/requestdisabletethering.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestsendptpcommand(_:outdata:sendcommanddelegate:didsendcommand:contextinfo:))*