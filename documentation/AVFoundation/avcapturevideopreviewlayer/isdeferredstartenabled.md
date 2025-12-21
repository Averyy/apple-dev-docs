# isDeferredStartEnabled

**Framework**: AVFoundation  
**Kind**: property

A `BOOL` value that indicates whether to defer starting this preview layer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isDeferredStartEnabled: Bool { get set }
```

#### Discussion

When this value is `true`, the session does not prepare the output’s resources until some time after [`startRunning()`](avcapturesession/startrunning().md) returns. You can start the visual parts of your user interface (e.g. preview) prior to other parts (e.g. photo/movie capture, metadata output, etc..) to improve startup performance. Set this value to `false` if your app needs video preview immediately for startup, and `true` if it does not.

By default, this value is `false` for [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) objects, since this object is used to display preview. For best session start performance, set [`isDeferredStartEnabled`](avcapturevideopreviewlayer/isdeferredstartenabled.md) to `false` for preview layers. If your app contains multiple preview layers, you may want to display the main preview layer as soon as possible and allow the remaining layers to display subsequently. In this case, set [`isDeferredStartEnabled`](avcapturevideopreviewlayer/isdeferredstartenabled.md) to `true` for the remaining layers.

> **Note**: Setting this property to the same value for all outputs, including [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) and [`AVCaptureOutput`](avcaptureoutput.md), is equivalent to not using deferred start.

If [`isDeferredStartSupported`](avcapturevideopreviewlayer/isdeferredstartsupported.md) is `false`, setting this property value to `true` results in the session throwing an `NSInvalidArgumentException`.

> **Note**: Set this value before calling [`commitConfiguration()`](avcapturesession/commitconfiguration().md) as it requires a lengthy reconfiguration of the capture render pipeline.

## See Also

- [var isDeferredStartSupported: Bool](avcapturevideopreviewlayer/isdeferredstartsupported.md)
  A `BOOL` value that indicates whether the preview layer supports deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/isdeferredstartenabled)*