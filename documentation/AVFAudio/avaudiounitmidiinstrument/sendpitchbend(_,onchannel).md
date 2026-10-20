# sendPitchBend(_:onChannel:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sends a MIDI Pitch Bend event to the instrument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)
```

```objc
- (void) sendPitchBend:(uint16_t) pitchbend onChannel:(uint8_t) channel;
```

#### Discussion

If this method isn’t invoked, then the system uses the default pitch bend value of `8192` (no pitch).

## Parameters

- `pitchbend`: Value of the pitchbend. The valid range of values is `0` to `16383`.
- `channel`: The channel number to send the event to. The valid range of values is `0` to `15`.

## See Also

### Sending MIDI events
- [func sendController(UInt8, withValue: UInt8, onChannel: UInt8)](./sendcontroller%28_,withvalue,onchannel%29.md)
  Sends a MIDI controller event to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8)](./sendmidievent%28_,data1%29.md)
  Sends a MIDI event which contains one data byte to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8, data2: UInt8)](./sendmidievent%28_,data1,data2%29.md)
  Sends a MIDI event which contains two data bytes to the instrument.
- [func sendMIDISysExEvent(Data)](./sendmidisysexevent%28_%29.md)
  Sends a MIDI System Exclusive event to the instrument.
- [func sendPressure(UInt8, onChannel: UInt8)](./sendpressure%28_,onchannel%29.md)
  Sends a MIDI channel pressure event to the instrument.
- [func sendPressure(forKey: UInt8, withValue: UInt8, onChannel: UInt8)](./sendpressure%28forkey,withvalue,onchannel%29.md)
  Sends a MIDI Polyphonic key pressure event to the instrument.
- [func sendProgramChange(UInt8, onChannel: UInt8)](./sendprogramchange%28_,onchannel%29.md)
  Sends MIDI Program Change and Bank Select events to the instrument.
- [func sendProgramChange(UInt8, bankMSB: UInt8, bankLSB: UInt8, onChannel: UInt8)](./sendprogramchange%28_,bankmsb,banklsb,onchannel%29.md)
  Sends MIDI Program Change and Bank Select events to the instrument.
- [func send(UnsafePointer<MIDIEventList>)](./send%28_%29.md)
  Sends a MIDI event list to the instrument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument/sendpitchbend(_:onchannel:))*