# dataOutputs

**Framework**: AVFoundation  
**Kind**: property

The list of data outputs governed by this data output synchronizer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var dataOutputs: [AVCaptureOutput] { get }
```

#### Discussion

This array is read-only. You configure the list of data outputs to synchronize only when you create an [`AVCaptureDataOutputSynchronizer`](avcapturedataoutputsynchronizer.md) object.

> **Note**:  The [`AVCaptureDataOutputSynchronizer`](avcapturedataoutputsynchronizer.md) class overrides the delegate (and delegate dispatch queue) settings of all of its data outputs, but video and depth data outputs still honor their [`alwaysDiscardsLateVideoFrames`](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) and [`alwaysDiscardsLateDepthData`](avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md) properties.

 The [`AVCaptureDataOutputSynchronizer`](avcapturedataoutputsynchronizer.md) class overrides the delegate (and delegate dispatch queue) settings of all of its data outputs, but video and depth data outputs still honor their [`alwaysDiscardsLateVideoFrames`](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) and [`alwaysDiscardsLateDepthData`](avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md) properties.

## See Also

- [init(dataOutputs: [AVCaptureOutput])](avcapturedataoutputsynchronizer/init(dataoutputs:).md)
  Creates a capture output synchronizer for the specified capture outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/dataoutputs)*