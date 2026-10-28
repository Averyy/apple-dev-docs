# layerWithSessionWithNoConnection:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new layer to preview the visual output of a capture session, without making connections to eligible video inputs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```objc
+ (instancetype) layerWithSessionWithNoConnection:(AVCaptureSession *) session;
```

## Return Value

A preview layer with no connections to a session’s eligible video inputs

## Discussion

Only use this initializer if you intend to manually connect the layer to a particular [`AVCaptureInput.Port`](../avcaptureinput/port.md) by calling the session’s [`addConnection(_:)`](../avcapturesession/addconnection%28_%29.md) method.

## Parameters

- `session`: A capture session to preview.

## See Also

### Creating a preview layer
- [+ layerWithSession:](./layerwithsession_.md)
  Returns a new layer to preview the visual output of a capture session.
- [init(session: AVCaptureSession)](./init%28session%29.md)
  Creates a layer to preview the visual output of a capture session.
- [init(sessionWithNoConnection: AVCaptureSession)](./init%28sessionwithnoconnection%29.md)
  Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsessionwithnoconnection:)*