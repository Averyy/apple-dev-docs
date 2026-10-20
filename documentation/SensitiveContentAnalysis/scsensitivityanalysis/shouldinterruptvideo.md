# shouldInterruptVideo

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Instance Property

Intervention guidance that suggests the app interrupt the video stream.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var shouldInterruptVideo: Bool { get }
```

```objc
@property (readonly) BOOL shouldInterruptVideo;
```

## See Also

### Receiving intervention guidance
- [var shouldIndicateSensitivity: Bool](./shouldindicatesensitivity.md)
  Intervention guidance that suggests the app indicate the presence of sensitive content.
- [var shouldMuteAudio: Bool](./shouldmuteaudio.md)
  Intervention guidance that suggests the app mute the audio of the current video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/shouldinterruptvideo)*