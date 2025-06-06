# setSessionWithNoConnection(_:)

**Framework**: AVFoundation  
**Kind**: method

Associates a session with the layer without automatically forming a connection to an eligible input port.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func setSessionWithNoConnection(_ session: AVCaptureSession)
```

#### Discussion

Only use this method if you intend to manually create a connection between the layer and a particular [`AVCaptureInput.Port`](avcaptureinput/port.md), and add it to the session using its [`addConnection(_:)`](avcapturesession/addconnection(_:).md) method.

## Parameters

- `session`: A capture session.

## See Also

- [var session: AVCaptureSession?](avcapturevideopreviewlayer/session.md)
  A capture session with visual output to preview.
- [var connection: AVCaptureConnection?](avcapturevideopreviewlayer/connection.md)
  An object that describes the connection from the layer to a particular input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/setsessionwithnoconnection(_:))*