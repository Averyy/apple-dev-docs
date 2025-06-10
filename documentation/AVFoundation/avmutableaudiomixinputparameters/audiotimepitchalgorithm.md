# audioTimePitchAlgorithm

**Framework**: AVFoundation  
**Kind**: property

The processing algorithm used to manage audio pitch for scaled audio edits.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm? { get set }
```

#### Discussion

The supported constants are defined in Time Pitch Algorithm Settings. An [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) is raised if this property is set to a value other than the defined constants.

## See Also

- [struct AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md)
  An algorithm used to set the audio pitch as the rate changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/audiotimepitchalgorithm)*