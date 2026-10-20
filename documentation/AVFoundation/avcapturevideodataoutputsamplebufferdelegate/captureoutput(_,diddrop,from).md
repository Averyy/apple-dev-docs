# captureOutput(_:didDrop:from:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that a video frame was discarded.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func captureOutput(_ output: AVCaptureOutput, didDrop sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection)
```

```objc
- (void) captureOutput:(AVCaptureOutput *) output didDropSampleBuffer:(CMSampleBufferRef) sampleBuffer fromConnection:(AVCaptureConnection *) connection;
```

#### Discussion

Delegates receive this message whenever a late video frame is dropped. This method is called once for each dropped frame. It is called on the dispatch queue specified by the output’s [`sampleBufferCallbackQueue`](../avcapturevideodataoutput/samplebuffercallbackqueue.md) property.

The `sampleBuffer` will contain a [`kCMSampleBufferAttachmentKey_DroppedFrameReason`](../../CoreMedia/kcmsamplebufferattachmentkey_droppedframereason.md) attachment that details why the frame was dropped. The frame may be dropped because it was late ([`kCMSampleBufferDroppedFrameReason_FrameWasLate`](../../CoreMedia/kcmsamplebufferdroppedframereason_framewaslate.md)), typically caused by the client’s processing taking too long. It can also be dropped because the module providing frames is out of buffers ([`kCMSampleBufferDroppedFrameReason_OutOfBuffers`](../../CoreMedia/kcmsamplebufferdroppedframereason_outofbuffers.md)). Frames can also be dropped if the module providing sample buffers has experienced a discontinuity ([`kCMSampleBufferDroppedFrameReason_Discontinuity`](../../CoreMedia/kcmsamplebufferdroppedframereason_discontinuity.md)) and an unknown number of frames have been lost.  This condition is typically caused by the system being too busy.

Because this method is called on the same dispatch queue that is responsible for outputting video frames, it must be efficient to prevent further capture performance problems, such as additional dropped video frames.

## Parameters

- `output`: The capture output object.
- `sampleBuffer`: A `CMSampleBuffer` object containing information about the dropped frame, such as its format and presentation time.

  This sample buffer contains none of the original video data.
- `connection`: The connection from which the video was received.

## See Also

### Managing sample buffer behavior
- [func captureOutput(AVCaptureOutput, didOutput: CMSampleBuffer, from: AVCaptureConnection)](./captureoutput%28_,didoutput,from%29.md)
  Notifies the delegate that a new video frame was written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:diddrop:from:))*