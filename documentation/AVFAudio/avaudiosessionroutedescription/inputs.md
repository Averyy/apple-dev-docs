# inputs

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of audio input port descriptions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var inputs: [AVAudioSessionPortDescription] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAudioSessionPortDescription *> * inputs;
```

#### Discussion

This property contains an array of [`AVAudioSessionPortDescription`](../avaudiosessionportdescription.md) objects representing the audio inputs associated with the current audio route for a session.

## See Also

### Getting the route’s ports
- [var outputs: [AVAudioSessionPortDescription]](./outputs.md)
  An array of audio output port descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionroutedescription/inputs)*