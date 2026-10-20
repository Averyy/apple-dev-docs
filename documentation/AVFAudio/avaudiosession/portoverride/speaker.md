# AVAudioSession.PortOverride.speaker

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A value that indicates to override the current inputs and outputs, and route audio to the built-in speaker and microphone.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
case speaker
```

```c
AVAudioSessionPortOverrideSpeaker
```

#### Discussion

This override type is only valid for the [`playAndRecord`](../category-swift.struct/playandrecord.md) category.

## See Also

### Choosing a port override
- [AVAudioSession.PortOverride.none](./none.md)
  A value that indicates not to override the output audio port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/portoverride/speaker)*