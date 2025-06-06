# init(audioComponentDescription:)

**Framework**: AVFAudio  
**Kind**: init

Creates a generator audio unit with the specified description.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(audioComponentDescription: AudioComponentDescription)
```

#### Return Value

A new `AVAudioUnitGenerator` instance.

#### Discussion

The [`AudioComponentDescription`](https://developer.apple.com/documentation/AudioToolbox/AudioComponentDescription) structure `componentType` field must be `kAudioUnitType_Generator` or [`kAudioUnitType_RemoteGenerator`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitType_RemoteGenerator).

## Parameters

- `audioComponentDescription`: The audio component description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitgenerator/init(audiocomponentdescription:))*