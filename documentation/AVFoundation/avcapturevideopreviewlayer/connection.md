# connection

**Framework**: AVFoundation  
**Kind**: property

An object that describes the connection from the layer to a particular input port.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var connection: AVCaptureConnection? { get }
```

## Mentions

- [Setting Up a Capture Session](setting-up-a-capture-session.md)

#### Discussion

When you associate a preview layer with a capture session, the session automatically creates a connection to the first eligible video [`AVCaptureInput.Port`](avcaptureinput/port.md) object. If you detach a preview layer from a session, the connection property becomes `nil`.

## See Also

- [var session: AVCaptureSession?](avcapturevideopreviewlayer/session.md)
  A capture session with visual output to preview.
- [func setSessionWithNoConnection(AVCaptureSession)](avcapturevideopreviewlayer/setsessionwithnoconnection(_:).md)
  Associates a session with the layer without automatically forming a connection to an eligible input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/connection)*