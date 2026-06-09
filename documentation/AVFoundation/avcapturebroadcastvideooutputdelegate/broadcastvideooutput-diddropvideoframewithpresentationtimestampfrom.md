# broadcastVideoOutput(_:didDropVideoFrameWithPresentationTimeStamp:from:)

**Framework**: AVFoundation  
**Kind**: method

Called when a video frame is dropped during broadcast video output processing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
optional func broadcastVideoOutput(_ output: AVCaptureBroadcastVideoOutput, didDropVideoFrameWithPresentationTimeStamp presentationTimeStamp: CMTime, from connection: AVCaptureConnection)
```

#### Discussion

This method is called whenever the broadcast video output system needs to drop a video frame due to performance constraints, destination issues, buffer overruns, or encoding failures.

## Parameters

- `output`: The [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) instance that dropped the video frame.
- `presentationTimeStamp`: The presentation timestamp (PTS) of the dropped video frame.
- `connection`: The [`AVCaptureConnection`](avcaptureconnection.md) associated with the dropped video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutputdelegate/broadcastvideooutput(_:diddropvideoframewithpresentationtimestamp:from:))*