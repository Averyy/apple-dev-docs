# audioTimePitchAlgorithm

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A processing algorithm for managing audio pitch for scaled audio edits.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm { get set }
```

```objc
@property (nonatomic, copy) AVAudioTimePitchAlgorithm audioTimePitchAlgorithm;
```

#### Discussion

The default value is [`spectral`](../avaudiotimepitchalgorithm/spectral.md).

## See Also

### Configuring audio output
- [var audioMix: AVAudioMix?](./audiomix.md)
  The parameters for audio mixing and an indication of whether to enable nondefault audio mixing for export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/audiotimepitchalgorithm)*