# channelAssignments

**Framework**: AVFAudio  
**Kind**: property

An array of channel descriptions associated with the audio recorder.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var channelAssignments: [AVAudioSessionChannelDescription]? { get set }
```

#### Discussion

The default value of this property is `nil`. When the value is non-`nil`, this value must have the same number of channels as defined in the [`settings`](avaudiorecorder/settings.md) property for the [`AVNumberOfChannelsKey`](avnumberofchannelskey.md) value. Use this property to help record specific audio channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/channelassignments)*