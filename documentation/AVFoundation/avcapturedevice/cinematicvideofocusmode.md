# AVCaptureDevice.CinematicVideoFocusMode

**Framework**: AVFoundation  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
enum CinematicVideoFocusMode
```

#### Overview

Constants indicating the focus behavior when recording a Cinematic Video.

Indicates that no focus mode is specified, in which case weak focus is used as default.

Indicates that the subject should remain in focus until it exits the scene.

Indicates that the Cinematic Video algorithm should automatically adjust focus according to the prominence of the subjects in the scene.

## Topics

### Enumeration Cases
- [AVCaptureDevice.CinematicVideoFocusMode.none](avcapturedevice/cinematicvideofocusmode/none.md)
- [AVCaptureDevice.CinematicVideoFocusMode.strong](avcapturedevice/cinematicvideofocusmode/strong.md)
- [AVCaptureDevice.CinematicVideoFocusMode.weak](avcapturedevice/cinematicvideofocusmode/weak.md)
### Initializers
- [init?(rawValue: Int)](avcapturedevice/cinematicvideofocusmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cinematicvideofocusmode)*