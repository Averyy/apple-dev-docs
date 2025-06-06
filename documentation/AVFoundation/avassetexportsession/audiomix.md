# audioMix

**Framework**: AVFoundation  
**Kind**: property

The parameters for audio mixing and an indication of whether to enable nondefault audio mixing for export.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
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

This value is key-value observable.

## See Also

- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avassetexportsession/audiotimepitchalgorithm.md)
  A processing algorithm for managing audio pitch for scaled audio edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/audiomix)*