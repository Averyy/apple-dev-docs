# setSessionWithNoConnection(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setSessionWithNoConnection:(AVCaptureSession *) session;
```

#### Discussion

Only use this method if you intend to manually create a connection between the layer and a particular [`AVCaptureInput.Port`](../avcaptureinput/port.md), and add it to the session using its [`addConnection(_:)`](../avcapturesession/addconnection%28_%29.md) method.

## Parameters

- `session`: A capture session.

## See Also

### Session configuration
- [var session: AVCaptureSession?](./session.md)
  A capture session with visual output to preview.
- [var connection: AVCaptureConnection?](./connection.md)
  An object that describes the connection from the layer to a particular input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/setsessionwithnoconnection(_:))*