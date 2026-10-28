# AVAudioUnitMIDIInstrument

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioUnitMIDIInstrument : AVAudioUnit
```

## Overview

Use an [`AVAudioUnitMIDIInstrument`](./avaudiounitmidiinstrument.md) in a chain that processes real-time (live) input and has the general concept of music events; for example, notes.

## Topics

### Creating a MIDI instrument
- [init(audioComponentDescription: AudioComponentDescription)](./avaudiounitmidiinstrument/init%28audiocomponentdescription%29.md)
  Creates a MIDI instrument audio unit with the component description you specify.
### Sending MIDI events
- [func sendController(UInt8, withValue: UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/sendcontroller%28_,withvalue,onchannel%29.md)
  Sends a MIDI controller event to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8)](./avaudiounitmidiinstrument/sendmidievent%28_,data1%29.md)
  Sends a MIDI event which contains one data byte to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8, data2: UInt8)](./avaudiounitmidiinstrument/sendmidievent%28_,data1,data2%29.md)
  Sends a MIDI event which contains two data bytes to the instrument.
- [func sendMIDISysExEvent(Data)](./avaudiounitmidiinstrument/sendmidisysexevent%28_%29.md)
  Sends a MIDI System Exclusive event to the instrument.
- [func sendPitchBend(UInt16, onChannel: UInt8)](./avaudiounitmidiinstrument/sendpitchbend%28_,onchannel%29.md)
  Sends a MIDI Pitch Bend event to the instrument.
- [func sendPressure(UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/sendpressure%28_,onchannel%29.md)
  Sends a MIDI channel pressure event to the instrument.
- [func sendPressure(forKey: UInt8, withValue: UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/sendpressure%28forkey,withvalue,onchannel%29.md)
  Sends a MIDI Polyphonic key pressure event to the instrument.
- [func sendProgramChange(UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/sendprogramchange%28_,onchannel%29.md)
  Sends MIDI Program Change and Bank Select events to the instrument.
- [func sendProgramChange(UInt8, bankMSB: UInt8, bankLSB: UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/sendprogramchange%28_,bankmsb,banklsb,onchannel%29.md)
  Sends MIDI Program Change and Bank Select events to the instrument.
- [func send(UnsafePointer<MIDIEventList>)](./avaudiounitmidiinstrument/send%28_%29.md)
  Sends a MIDI event list to the instrument.
### Starting and stopping play
- [func startNote(UInt8, withVelocity: UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/startnote%28_,withvelocity,onchannel%29.md)
  Sends a MIDI Note On event to the instrument.
- [func stopNote(UInt8, onChannel: UInt8)](./avaudiounitmidiinstrument/stopnote%28_,onchannel%29.md)
  Sends a MIDI Note Off event to the instrument.

## Relationships

### Inherits From
- [AVAudioUnit](./avaudiounit.md)
### Inherited By
- [AVAudioUnitSampler](./avaudiounitsampler.md)
### Conforms To
- [AVAudio3DMixing](./avaudio3dmixing.md)
- [AVAudioMixing](./avaudiomixing.md)
- [AVAudioStereoMixing](./avaudiostereomixing.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument)*