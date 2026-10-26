# channelVoice1

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

active when type is kMIDIMessageTypeChannelVoice1

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
struct { ... } channelVoice1;
```

## Topics

### Instance Properties
- [channel](./channelvoice1-20x9n/channel.md)
  MIDI channel 0-15
- [channelPressure](./channelvoice1-20x9n/channelpressure.md)
  7 bit channel pressure, active when status is kMIDICVStatusChannelPressure
- [controlChange](./channelvoice1-20x9n/controlchange.md)
  active when status is kMIDICVStatusControlChange
- [note](./channelvoice1-20x9n/note.md)
  active when status is kMIDICVStatusNoteOff or kMIDICVStatusNoteOn
- [pitchBend](./channelvoice1-20x9n/pitchbend.md)
  7 bit pitch bend active when status is kMIDICVStatusPitchBend
- [polyPressure](./channelvoice1-20x9n/polypressure.md)
  active when status is kMIDICVStatusPolyPressure
- [program](./channelvoice1-20x9n/program.md)
  7 bit program nr, active when status is kMIDICVStatusProgramChange
- [reserved](./channelvoice1-20x9n/reserved.md)
- [status](./channelvoice1-20x9n/status.md)
  determines which variant is active


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiuniversalmessage/channelvoice1-20x9n)*