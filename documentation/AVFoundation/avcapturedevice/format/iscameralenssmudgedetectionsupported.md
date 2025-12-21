# isCameraLensSmudgeDetectionSupported

**Framework**: AVFoundation  
**Kind**: property

Whether camera lens smudge detection is supported.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isCameraLensSmudgeDetectionSupported: Bool { get }
```

#### Discussion

This property returns `true` if the session’s current configuration supports lens smudge detection. When switching cameras or formats, this property may change. When this property changes from `true` to `false`, [`isCameraLensSmudgeDetectionEnabled`](avcapturedevice/iscameralenssmudgedetectionenabled.md) also reverts to `false`. If you opt in for lens smudge detection and then change configurations, you should set [`isCameraLensSmudgeDetectionEnabled`](avcapturedevice/iscameralenssmudgedetectionenabled.md) to `true` again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscameralenssmudgedetectionsupported)*