# shouldMuteAudio

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Instance Property

Intervention guidance that suggests the app mute the audio of the current video stream.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var shouldMuteAudio: Bool { get }
```

```objc
@property (readonly) BOOL shouldMuteAudio;
```

## See Also

### Receiving intervention guidance
- [var shouldIndicateSensitivity: Bool](./shouldindicatesensitivity.md)
  Intervention guidance that suggests the app indicate the presence of sensitive content.
- [var shouldInterruptVideo: Bool](./shouldinterruptvideo.md)
  Intervention guidance that suggests the app interrupt the video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/shouldmuteaudio)*