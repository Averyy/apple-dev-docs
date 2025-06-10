# defaultCaptureSoundDisabled

**Framework**: AVKit  
**Kind**: property

A boolean value indicating whether or not the default sound is disabled.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class var defaultCaptureSoundDisabled: Bool { get set }
```

#### Discussion

If `YES`, sound playback for capture events must be handled manually using the `playSound` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/defaultcapturesounddisabled)*