# cinematicVideoMetadata

**Framework**: AVFoundation  
**Kind**: property

A constant that identifies Cinematic video metadata for post-capture Cinematic video editing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
static let cinematicVideoMetadata: AVMetadataObject.ObjectType
```

#### Discussion

This metadata object type is only available when the source [`AVCaptureDevice`](avcapturedevice.md)’s `activeFormat` has `AVCaptureDeviceFormat/isCinematicVideoMetadataCaptureSupported` equal to `true`. It can therefore appear and disappear from [`availableMetadataObjectTypes`](avcapturemetadataoutput/availablemetadataobjecttypes.md) as the active format changes; observers should not assume it is statically available for the lifetime of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objecttype/cinematicvideometadata)*