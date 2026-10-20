# lowNote

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The note value below which the system filters out notes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var lowNote: UInt8
```

```c
UInt8 lowNote;
```

## See Also

### Connection Parameters
- [var noteNumber: MIDITransform](./notenumber.md)
  The transformation of MIDI note numbers.
- [var highNote: UInt8](./highnote.md)
  The note value above which the system filters out notes.
- [var velocity: MIDITransform](./velocity.md)
  A note velocity transformation.
- [var lowVelocity: UInt8](./lowvelocity.md)
  The velocity value below which the system filters out notes.
- [var highVelocity: UInt8](./highvelocity.md)
  The velocity value above which the system filters out notes.
- [var keyPressure: MIDITransform](./keypressure.md)
  The transformation of polyphonic key pressure events.
- [var channelPressure: MIDITransform](./channelpressure.md)
  The transformation of MIDI monophonic channel pressure events.
- [var version: UInt32](./version.md)
  The version number.
- [var numSources: UInt32](./numsources.md)
  The number of valid sources.
- [var sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)](./sources.md)
  All MIDI sources for this connection.
- [var numDestinations: UInt32](./numdestinations.md)
  The number of valid destinations.
- [var destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)](./destinations.md)
  All MIDI destinations for this connection.
- [var channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./channelmap.md)
  A mapping of MIDI channels.
- [var filterOutAllControls: UInt8](./filteroutallcontrols.md)
  A value that indicates whether to filter out MIDI continuous control messages.
- [var filterOutBeatClock: UInt8](./filteroutbeatclock.md)
  A value that indicates whether to filter out MIDI clock, play, stop, and resume messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparams/lownote)*