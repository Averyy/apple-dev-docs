# isCinematicVideoMetadataCaptureSupported

**Framework**: AVFoundation  
**Kind**: property

Returns whether capturing cinematic video metadata to the movie file is supported in the current session configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isCinematicVideoMetadataCaptureSupported: Bool { get }
```

#### Discussion

Cinematic video metadata enables post-capture cinematic video editing using the Cinematic framework.

This property returns `true` when all of the following conditions are met:

- The source device’s `activeFormat` supports cinematic video metadata capture.
- The source device’s dynamic aspect ratio is 16:9 or 9:16 (or unset).
- Spatial video capture (`spatialVideoCaptureEnabled`) is not enabled.
- No other incompatible features are enabled.

When switching cameras, formats, or toggling other features, this property may change. This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/iscinematicvideometadatacapturesupported)*