# captureHighResolutionFrame(completion:)

**Framework**: ARKit  
**Kind**: method

Requests a frame outside of the normal frequency that contains a high-resolution captured image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureHighResolutionFrame() async throws -> ARFrame
```

#### Discussion

If the function succeeds, the completion handler’s frame contains a high quality, high resolution [`capturedImage`](arframe/capturedimage.md).

In the event of failure, the completion block receives a non-`nil` error object. A call may fail if a previous request for a high resolution capture hasn’t completed yet, or an underlying problem occurs in the system’s capture pipeline. You can identify the failure reason in either case by checking for [`highResolutionFrameCaptureInProgress`](arerror/highresolutionframecaptureinprogress.md) or [`highResolutionFrameCaptureFailed`](arerror/highresolutionframecapturefailed.md), respectively.

ARKit populates the frame’s properties other than pixel data, including pose information, anchors, and frame semantics. The system provides the frame to your completion handler asynchronously.

You can call this function at any time during a session. The system delivers a high-resolution frame out-of-band, which means that it doesn’t affect the other frames that the session receives at a regular interval, such as [`currentFrame`](arsession/currentframe.md) or the frame argument to [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-9v2kw.md).

For the highest resolution captured image, choose a non-binned [`videoFormat`](arconfiguration/videoformat-swift.property.md) in your session’s configuration. You can call [`recommendedVideoFormatForHighResolutionFrameCapturing`](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md) to select the best option for you.

For the highest resolution still images, choose a [`videoFormat`](arconfiguration/videoformat-swift.property.md) among your configuration’s [`supportedVideoFormats`](arconfiguration/supportedvideoformats.md) that returns `true` for [`isRecommendedForHighResolutionFrameCapturing`](arconfiguration/videoformat-swift.class/isrecommendedforhighresolutionframecapturing.md). If your app doesn’t have specific resolution requirements, you can use the framework-recommended format that [`recommendedVideoFormatForHighResolutionFrameCapturing`](arconfiguration/recommendedvideoformatforhighresolutionframecapturing.md) returns.

## Parameters

- `completion`: Code you provide that the framework runs after attempting to generate the frame.

## See Also

- [var currentFrame: ARFrame?](arsession/currentframe.md)
  The most recent still frame captured by the active camera feed, including ARKit’s interpretation of it.
- [class ARFrame](arframe.md)
  A video image captured as part of a session with position-tracking information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/capturehighresolutionframe(completion:))*