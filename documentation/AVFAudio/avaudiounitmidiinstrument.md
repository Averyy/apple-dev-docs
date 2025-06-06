# AVAudioUnitMIDIInstrument

**Framework**: AVFAudio  
**Kind**: class

An object that represents music devices or remote instruments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitMIDIInstrument
```

#### Overview

Use an [`AVAudioUnitMIDIInstrument`](avaudiounitmidiinstrument.md) in a chain that processes real-time (live) input and has the general concept of music events; for example, notes.

## Topics

### Creating a MIDI instrument
- [init(audioComponentDescription: AudioComponentDescription)](avaudiounitmidiinstrument/init(audiocomponentdescription:).md)
  Creates a MIDI instrument audio unit with the component description you specify.
### Sending information to the MIDI instrument
- [func sendController(UInt8, withValue: UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/sendcontroller(_:withvalue:onchannel:).md)
  Sends a MIDI controller event to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8)](avaudiounitmidiinstrument/sendmidievent(_:data1:).md)
  Sends a MIDI event which contains one data byte to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8, data2: UInt8)](avaudiounitmidiinstrument/sendmidievent(_:data1:data2:).md)
  Sends a MIDI event which contains two data bytes to the instrument.
- [func sendMIDISysExEvent(Data)](avaudiounitmidiinstrument/sendmidisysexevent(_:).md)
  Sends a MIDI System Exclusive event to the instrument.
- [func sendPitchBend(UInt16, onChannel: UInt8)](avaudiounitmidiinstrument/sendpitchbend(_:onchannel:).md)
  Sends a MIDI Pitch Bend event to the instrument.
- [func sendPressure(UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/sendpressure(_:onchannel:).md)
  Sends a MIDI channel pressure event to the instrument.
- [func sendPressure(forKey: UInt8, withValue: UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/sendpressure(forkey:withvalue:onchannel:).md)
  Sends a MIDI Polyphonic key pressure event to the instrument.
- [func sendProgramChange(UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/sendprogramchange(_:onchannel:).md)
  Sends MIDI Program Change and Bank Select events to the instrument.
- [func sendProgramChange(UInt8, bankMSB: UInt8, bankLSB: UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/sendprogramchange(_:bankmsb:banklsb:onchannel:).md)
  Sends MIDI Program Change and Bank Select events to the instrument.
- [func send(UnsafePointer<MIDIEventList>)](avaudiounitmidiinstrument/send(_:).md)
  Sends a MIDI event list to the instrument.
### Starting and stopping play
- [func startNote(UInt8, withVelocity: UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/startnote(_:withvelocity:onchannel:).md)
  Sends a MIDI Note On event to the instrument.
- [func stopNote(UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/stopnote(_:onchannel:).md)
  Sends a MIDI Note Off event to the instrument.

## Relationships

### Inherits From
- [AVAudioUnit](avaudiounit.md)
### Inherited By
- [AVAudioUnitSampler](avaudiounitsampler.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument)*