# layerWithSession:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new layer to preview the visual output of a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```objc
+ (instancetype) layerWithSession:(AVCaptureSession *) session;
```

## Return Value

A preview layer.

## Parameters

- `session`: The capture session from which to source the preview.

## See Also

### Creating a preview layer
- [init(session: AVCaptureSession)](./init%28session%29.md)
  Creates a layer to preview the visual output of a capture session.
- [+ layerWithSessionWithNoConnection:](./layerwithsessionwithnoconnection_.md)
  Returns a new layer to preview the visual output of a capture session, without making connections to eligible video inputs.
- [init(sessionWithNoConnection: AVCaptureSession)](./init%28sessionwithnoconnection%29.md)
  Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsession:)*