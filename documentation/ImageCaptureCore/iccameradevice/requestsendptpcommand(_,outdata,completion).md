# requestSendPTPCommand(_:outData:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Sends a Picture Transfer Protocol (PTP) command to a camera asynchronously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestSendPTPCommand(_ ptpCommand: Data, outData ptpData: Data?, completion: @escaping @Sendable (Data, Data, (any Error)?) -> Void)
```

```swift
func requestSendPTPCommand(_ ptpCommand: Data, outData ptpData: Data?) async throws -> (Data, Data)
```

```objc
- (void) requestSendPTPCommand:(NSData *) ptpCommand outData:(NSData *) ptpData completion:(void (^)(NSData *responseData, NSData *ptpResponseData, NSError *error)) completion;
```

## Discussion

The block receives the response, data, and an error message, if present.

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
- [func requestDisableTethering()](./requestdisabletethering%28%29.md)
  Disables tethered capture on the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestsendptpcommand(_:outdata:completion:))*