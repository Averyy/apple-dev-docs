# audioMix

**Framework**: AVFoundation  
**Kind**: property

The audio mix to use with this output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var audioMix: AVAudioMix? { get set }
```

#### Discussion

Use an audio mix to specify how an audio track’s volume changes over the media’s timeline.

## See Also

- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avassetreaderaudiomixoutput/audiotimepitchalgorithm.md)
  The processing algorithm to use for scaled audio edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiomix)*