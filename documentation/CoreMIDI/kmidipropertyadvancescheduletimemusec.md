# kMIDIPropertyAdvanceScheduleTimeMuSec

**Framework**: Core MIDI  
**Kind**: var

The recommended number of microseconds in advance that clients should schedule output.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyAdvanceScheduleTimeMuSec: CFString
```

#### Discussion

Only the driver that owns the object may set this property.

If this property value is nonzero, clients should treat the value as a minimum. For devices with a nonzero advance schedule time, drivers receive outgoing messages to the device at the time the client sends them using [`MIDISend(_:_:_:)`](midisend(_:_:_:).md). The driver is responsible for scheduling events to play at the right times, according to their timestamps.

You can also set this property on any virtual destinations you create. When clients send messages to a virtual destination with an advance schedule time of 0, the destination receives the messages at the scheduled delivery time. If a virtual destination has a nonzero advance schedule time, it receives timestamped messages as soon as they’re sent, and must do its own internal scheduling of events it receives.

## See Also

- [let kMIDIPropertyTransmitsMTC: CFString](kmidipropertytransmitsmtc.md)
  A Boolean value that indicates whether the device or entity transmits MIDI Time Code messages.
- [let kMIDIPropertyReceivesMTC: CFString](kmidipropertyreceivesmtc.md)
  A Boolean value that indicates whether the device or entity responds to MIDI Time Code messages.
- [let kMIDIPropertyTransmitsClock: CFString](kmidipropertytransmitsclock.md)
  A Boolean value that indicates whether the device or entity transmits MIDI beat clock messages.
- [let kMIDIPropertyReceivesClock: CFString](kmidipropertyreceivesclock.md)
  A Boolean value that indicates whether the device or entity responds to MIDI beat clock messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyadvancescheduletimemusec)*