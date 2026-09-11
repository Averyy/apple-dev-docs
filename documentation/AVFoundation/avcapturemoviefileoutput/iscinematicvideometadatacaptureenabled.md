# isCinematicVideoMetadataCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property

Indicates whether cinematic video metadata is captured to movie files.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isCinematicVideoMetadataCaptureEnabled: Bool { get set }
```

#### Discussion

When `true`, recorded movie files include a cinematic video metadata track that enables post-capture cinematic video editing using the Cinematic framework.

This property may only be set when `automaticallyAdjustsCinematicVideoMetadataCaptureEnabled` is `false`. Setting this property when `automaticallyAdjustsCinematicVideoMetadataCaptureEnabled` is `true` throws an `NSInvalidArgumentException`.

This property may only be set to `true` when `cinematicVideoMetadataCaptureSupported` is `true`. Setting to `true` when not supported throws an `NSInvalidArgumentException`.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/iscinematicvideometadatacaptureenabled)*