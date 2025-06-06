# isPreviewing

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the layer is rendering video frames from its source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isPreviewing: Bool { get }
```

#### Discussion

A preview layer begins displaying content when you call the capture session’s [`startRunning()`](avcapturesession/startrunning().md) method. If you associate the layer with an instance of [`AVCaptureMultiCamSession`](avcapturemulticamsession.md), the system guarantees that all video preview layers display content by the time the blocking call to [`startRunning()`](avcapturesession/startrunning().md) or [`commitConfiguration()`](avcapturesession/commitconfiguration().md) returns.

While a session is running, you may enable or disable a video preview layer’s connection to start or stop the flow of video to the layer. You may key-value observe the connection’s [`isEnabled`](avcaptureconnection/isenabled.md) property to observe this property changing, and synchronize any user interface changes to take place precisely when the video resumes rendering to the video preview layer.

## See Also

- [var videoGravity: AVLayerVideoGravity](avcapturevideopreviewlayer/videogravity.md)
  A value that indicates how the layer displays video content within its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/ispreviewing)*