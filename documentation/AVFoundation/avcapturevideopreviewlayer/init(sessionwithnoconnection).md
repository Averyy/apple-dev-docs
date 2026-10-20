# init(sessionWithNoConnection:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSessionWithNoConnection:(AVCaptureSession *) session;
```

#### Discussion

Only use this initializer if you intend to manually connect the layer to a particular [`AVCaptureInput.Port`](../avcaptureinput/port.md) by calling the session’s [`addConnection(_:)`](../avcapturesession/addconnection%28_%29.md) method.

## Parameters

- `session`: A capture session to preview.

## See Also

### Creating a preview layer
- [init(session: AVCaptureSession)](./init%28session%29.md)
  Creates a layer to preview the visual output of a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/init(sessionwithnoconnection:))*