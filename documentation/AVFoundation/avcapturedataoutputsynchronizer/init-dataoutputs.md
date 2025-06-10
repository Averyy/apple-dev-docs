# init(dataOutputs:)

**Framework**: AVFoundation  
**Kind**: init

Creates a capture output synchronizer for the specified capture outputs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
init(dataOutputs: [AVCaptureOutput])
```

#### Discussion

The first output in the array acts as the main data output and determines when the synchronized callback is delivered. When data is received for the main data output, the synchronizer holds that data until all other data outputs have received data with an equal or later presentation timestamp, or determines that there is no data for a particular output at the main data output’s presentation timestamp. After collecting data from all outputs, the synchronizer sends a single delegate callback, containing all the data aligned with the main data output’s data. If the capture system receives data with presentation timestamps earlier than the next main data output time, the synchronizer sends separate delegate callbacks.

For example, if you specify a video data output as your first (main) output and a metadata output for detected faces as your second output, your data callback is not called until there is face data ready for a corresponding video frame, or it is assured that there is no face metadata for that particular video frame.

> **Note**:  The [`AVCaptureDataOutputSynchronizer`](avcapturedataoutputsynchronizer.md) class overrides the delegate (and delegate dispatch queue) settings of all of its data outputs, but video and depth data outputs still honor their [`alwaysDiscardsLateVideoFrames`](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) and [`alwaysDiscardsLateDepthData`](avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md) properties.

## Parameters

- `dataOutputs`: An array of capture output objects. The first object in this array is treated as the main output to which all others are synchronized.

## See Also

- [var dataOutputs: [AVCaptureOutput]](avcapturedataoutputsynchronizer/dataoutputs.md)
  The list of data outputs governed by this data output synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/init(dataoutputs:))*