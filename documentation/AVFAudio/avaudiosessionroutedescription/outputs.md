# outputs

**Framework**: AVFAudio  
**Kind**: property

An array of audio output port descriptions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outputs: [AVAudioSessionPortDescription] { get }
```

#### Discussion

This property contains an array of [`AVAudioSessionPortDescription`](avaudiosessionportdescription.md) objects representing the audio outputs associated with the current audio route for a session.

## See Also

- [var inputs: [AVAudioSessionPortDescription]](avaudiosessionroutedescription/inputs.md)
  An array of audio input port descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionroutedescription/outputs)*