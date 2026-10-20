# sendController(_:withValue:onChannel:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sends a MIDI controller event to the instrument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)
```

```objc
- (void) sendController:(uint8_t) controller withValue:(uint8_t) value onChannel:(uint8_t) channel;
```

## Parameters

- `controller`: Specifies a standard MIDI controller number. The valid range is `0` to `127`.
- `value`: Value for the controller. The valid range is `0` to `127`.
- `channel`: The channel number to send the event to. The valid range is `0` to `15`.

## See Also

### Sending MIDI events
- [func sendMIDIEvent(UInt8, data1: UInt8)](./sendmidievent%28_,data1%29.md)
  Sends a MIDI event which contains one data byte to the instrument.
- [func sendMIDIEvent(UInt8, data1: UInt8, data2: UInt8)](./sendmidievent%28_,data1,data2%29.md)
  Sends a MIDI event which contains two data bytes to the instrument.
- [func sendMIDISysExEvent(Data)](./sendmidisysexevent%28_%29.md)
  Sends a MIDI System Exclusive event to the instrument.
- [func sendPitchBend(UInt16, onChannel: UInt8)](./sendpitchbend%28_,onchannel%29.md)
  Sends a MIDI Pitch Bend event to the instrument.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument/sendcontroller(_:withvalue:onchannel:))*