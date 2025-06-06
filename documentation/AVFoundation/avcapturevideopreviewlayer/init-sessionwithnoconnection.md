# init(sessionWithNoConnection:)

**Framework**: AVFoundation  
**Kind**: init

Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
init(sessionWithNoConnection session: AVCaptureSession)
```

#### Discussion

Only use this initializer if you intend to manually connect the layer to a particular [`AVCaptureInput.Port`](avcaptureinput/port.md) by calling the session’s [`addConnection(_:)`](avcapturesession/addconnection(_:).md) method.

## Parameters

- `session`: A capture session to preview.

## See Also

- [init(session: AVCaptureSession)](avcapturevideopreviewlayer/init(session:).md)
  Creates a layer to preview the visual output of a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/init(sessionwithnoconnection:))*