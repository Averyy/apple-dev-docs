# channelVoice2

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

active when type is kMIDIMessageTypeChannelVoice2

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
struct { ... } channelVoice2;
```

## Topics

### Instance Properties
- [channel](./channelvoice2-20x9k/channel.md)
  MIDI channel
- [channelPressure](./channelvoice2-20x9k/channelpressure.md)
  active when status is kMIDICVStatusChannelPressure
- [controlChange](./channelvoice2-20x9k/controlchange.md)
  active when status is kMIDICVStatusControlChange
- [controller](./channelvoice2-20x9k/controller.md)
  active when status is any of kMIDICVStatusRegisteredControl, kMIDICVStatusAssignableControl, kMIDICVStatusRelRegisteredControl, or kMIDICVStatusRelAssignableControl
- [note](./channelvoice2-20x9k/note.md)
  active when status is kMIDICVStatusNoteOff or kMIDICVStatusNoteOn
- [perNoteController](./channelvoice2-20x9k/pernotecontroller.md)
  active when status is kMIDICVStatusRegisteredPNC or kMIDICVStatusAssignablePNC
- [perNoteManagement](./channelvoice2-20x9k/pernotemanagement.md)
  active when status is kMIDICVStatusPerNoteMgmt
- [perNotePitchBend](./channelvoice2-20x9k/pernotepitchbend.md)
  active when status is kMIDICVStatusPerNotePitchBend
- [pitchBend](./channelvoice2-20x9k/pitchbend.md)
  active when status is kMIDICVStatusPitchBend
- [polyPressure](./channelvoice2-20x9k/polypressure.md)
  active when status is kMIDICVStatusPolyPressure
- [programChange](./channelvoice2-20x9k/programchange.md)
  active when status is kMIDICVStatusProgramChange
- [reserved](./channelvoice2-20x9k/reserved.md)
- [status](./channelvoice2-20x9k/status.md)
  determines which variant is active


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiuniversalmessage/channelvoice2-20x9k)*