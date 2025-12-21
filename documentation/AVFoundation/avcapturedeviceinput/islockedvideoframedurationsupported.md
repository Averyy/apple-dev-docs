# isLockedVideoFrameDurationSupported

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the device input supports locked frame durations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isLockedVideoFrameDurationSupported: Bool { get }
```

#### Discussion

See [`activeLockedVideoFrameDuration`](avcapturedeviceinput/activelockedvideoframeduration.md) for more information on video frame duration locking.

## See Also

- [var activeLockedVideoFrameDuration: CMTime](avcapturedeviceinput/activelockedvideoframeduration.md)
  The receiver’s locked frame duration (the reciprocal of its frame rate). Setting this property guarantees the intra-frame duration delivered by the device input is precisely the frame duration you request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/islockedvideoframedurationsupported)*