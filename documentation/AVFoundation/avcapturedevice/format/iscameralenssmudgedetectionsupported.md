# isCameraLensSmudgeDetectionSupported

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var isCameraLensSmudgeDetectionSupported: Bool { get }
```

#### Discussion

A BOOL value specifying whether camera lens smudge detection is supported.

This property returns YES if the session’s current configuration supports lens smudge detection. When switching cameras or formats this property may change. When this property changes from YES to NO, cameraLensSmudgeDetectionEnabled also reverts to NO. If you’ve previously opted in for lens smudge detection and then change configurations, you may need to set cameraLensSmudgeDetectionEnabled = YES again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscameralenssmudgedetectionsupported)*