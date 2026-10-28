# audioTimePitchAlgorithm

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The processing algorithm to use for scaled audio edits.

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

## Discussion

See [Time pitch algorithm settings](../time-pitch-algorithm-settings.md) for possible values. The system throws an exception if you set this property to a value other than one of the defined constants.

## See Also

### Configuring audio settings
- [var audioMix: AVAudioMix?](./audiomix.md)
  The audio mix to use with this output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiotimepitchalgorithm)*