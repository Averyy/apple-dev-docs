# depthDataOutput(_:didOutput:timestamp:connection:)

**Framework**: AVFoundation  
**Kind**: method

Provides newly captured depth data to the delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func depthDataOutput(_ output: AVCaptureDepthDataOutput, didOutput depthData: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection)
```

#### Discussion

The depth data output calls this method whenever it captures and outputs a new depth data object. This method is called on the dispatch queue specified by the output’s [`delegateCallbackQueue`](avcapturedepthdataoutput/delegatecallbackqueue.md) property, and can be called frequently. Your implementation must process the depth data quickly in order to prevent dropped depth data.

To maintain optimal performance, the capture pipeline may allocate [`AVDepthData`](avdepthdata.md) pixel buffer maps from a finite memory pool. If you hold on to any [`AVDepthData`](avdepthdata.md) objects for too long, capture inputs cannot copy new depth data into memory, resulting in dropped depth data. If your application is causing depth data drops by holding on to provided depth data objects for too long, consider copying the pixel buffer map data into a new pixel buffer so that the [`AVDepthData`](avdepthdata.md) backing memory can be reused more quickly.

## Parameters

- `output`: The depth data output providing data.
- `depthData`: A depth data object containing the captured per-pixel depth data.
- `timestamp`: The time at which the data was captured.
- `connection`: The capture connection through which the data was captured.

## See Also

- [func depthDataOutput(AVCaptureDepthDataOutput, didDrop: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection, reason: AVCaptureOutput.DataDroppedReason)](avcapturedepthdataoutputdelegate/depthdataoutput(_:diddrop:timestamp:connection:reason:).md)
  Informs the delegate that captured depth data was not processed.
- [AVCaptureOutput.DataDroppedReason](avcaptureoutput/datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:))*