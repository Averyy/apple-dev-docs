# sendProgramChange(_:bankMSB:bankLSB:onChannel:)

**Framework**: AVFAudio  
**Kind**: method

Sends MIDI Program Change and Bank Select events to the instrument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func sendProgramChange(_ program: UInt8, bankMSB: UInt8, bankLSB: UInt8, onChannel channel: UInt8)
```

## Parameters

- `program`: Specifies the program (preset) number within the bank to load. The valid range is   to  .
- `bankMSB`: Specifies the most significant byte value for the bank to select. The valid range is   to  .
- `bankLSB`: Specifies the least significant byte value for the bank to select. The valid range is   to  .
- `channel`: The channel number to send the event to. The valid range is   to  .

## See Also

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
- [func send(UnsafePointer<MIDIEventList>)](avaudiounitmidiinstrument/send(_:).md)
  Sends a MIDI event list to the instrument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument/sendprogramchange(_:bankmsb:banklsb:onchannel:))*