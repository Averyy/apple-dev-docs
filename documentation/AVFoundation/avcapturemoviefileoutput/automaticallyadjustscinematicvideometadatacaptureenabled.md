# automaticallyAdjustsCinematicVideoMetadataCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property

Controls whether cinematic video metadata capture is automatically managed by the framework.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var automaticallyAdjustsCinematicVideoMetadataCaptureEnabled: Bool { get set }
```

#### Discussion

When this property is `true` (the default), the framework manages `cinematicVideoMetadataCaptureEnabled` automatically. The framework decides when to enable cinematic video metadata capture; capture is not guaranteed even when `cinematicVideoMetadataCaptureSupported` is `true`. Clients that need explicit control over whether metadata is captured should set this property to `false` and manage `cinematicVideoMetadataCaptureEnabled` directly.

When this property is `false`, `cinematicVideoMetadataCaptureEnabled` is not automatically managed and must be explicitly set by the client.

Setting this property from `true` to `false` sets `cinematicVideoMetadataCaptureEnabled` to `false`.

This property can be set before calling `-[AVCaptureSession startRunning]` or within `-[AVCaptureSession beginConfiguration]` and `-[AVCaptureSession commitConfiguration]` while the session is running.

Default value: `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/automaticallyadjustscinematicvideometadatacaptureenabled)*