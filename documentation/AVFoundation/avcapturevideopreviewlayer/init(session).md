# init(session:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a layer to preview the visual output of a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
init(session: AVCaptureSession)
```

```objc
- (instancetype) initWithSession:(AVCaptureSession *) session;
```

## Parameters

- `session`: A capture session to preview.

## See Also

### Creating a preview layer
- [init(sessionWithNoConnection: AVCaptureSession)](./init%28sessionwithnoconnection%29.md)
  Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.
- [+ layerWithSession:](./layerwithsession_.md)
  Returns a new layer to preview the visual output of a capture session.
- [+ layerWithSessionWithNoConnection:](./layerwithsessionwithnoconnection_.md)
  Returns a new layer to preview the visual output of a capture session, without making connections to eligible video inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/init(session:))*