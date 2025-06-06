# init(audioComponentDescription:)

**Framework**: AVFAudio  
**Kind**: init

Creates a MIDI instrument audio unit with the component description you specify.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(audioComponentDescription description: AudioComponentDescription)
```

#### Return Value

A new [`AVAudioUnitMIDIInstrument`](avaudiounitmidiinstrument.md) instance.

#### Discussion

The component type must be `kAudioUnitType_MusicDevice` or `kAudioUnitType_RemoteInstrument`.

## Parameters

- `description`: The description of the audio component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument/init(audiocomponentdescription:))*