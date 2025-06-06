# AVCaptureOutput.DataDroppedReason.lateData

**Framework**: AVFoundation  
**Kind**: case

The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case lateData
```

#### Discussion

Use the [`alwaysDiscardsLateVideoFrames`](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) property of [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) or the [`alwaysDiscardsLateDepthData`](avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md) property of [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) to choose whether the capture output discards data.

## See Also

- [AVCaptureOutput.DataDroppedReason.none](avcaptureoutput/datadroppedreason/none.md)
  The system didn’t drop data.
- [AVCaptureOutput.DataDroppedReason.outOfBuffers](avcaptureoutput/datadroppedreason/outofbuffers.md)
  The system dropped data because the capture output exhausted its internal pool of memory buffers.
- [AVCaptureOutput.DataDroppedReason.discontinuity](avcaptureoutput/datadroppedreason/discontinuity.md)
  The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason/latedata)*