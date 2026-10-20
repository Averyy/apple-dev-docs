# isCinematicVideoMetadataCaptureSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the format supports Cinematic Video Metadata capture.

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

```objc
@property (nonatomic, readonly, getter=isCinematicVideoMetadataCaptureSupported) BOOL cinematicVideoMetadataCaptureSupported;
```

#### Discussion

This property returns `true` if the format supports capturing cinematic video metadata alongside video. The metadata enables post-capture cinematic video editing using the Cinematic framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscinematicvideometadatacapturesupported)*