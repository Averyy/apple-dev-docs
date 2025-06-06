# velocity

**Framework**: Core MIDI  
**Kind**: property

A note velocity transformation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var velocity: MIDITransform
```

## See Also

- [var noteNumber: MIDITransform](midithruconnectionparams/notenumber.md)
  The transformation of MIDI note numbers.
- [var lowNote: UInt8](midithruconnectionparams/lownote.md)
  The note value below which the system filters out notes.
- [var highNote: UInt8](midithruconnectionparams/highnote.md)
  The note value above which the system filters out notes.
- [var lowVelocity: UInt8](midithruconnectionparams/lowvelocity.md)
  The velocity value below which the system filters out notes.
- [var highVelocity: UInt8](midithruconnectionparams/highvelocity.md)
  The velocity value above which the system filters out notes.
- [var keyPressure: MIDITransform](midithruconnectionparams/keypressure.md)
  The transformation of polyphonic key pressure events.
- [var channelPressure: MIDITransform](midithruconnectionparams/channelpressure.md)
  The transformation of MIDI monophonic channel pressure events.
- [var version: UInt32](midithruconnectionparams/version.md)
  The version number.
- [var numSources: UInt32](midithruconnectionparams/numsources.md)
  The number of valid sources.
- [var sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)](midithruconnectionparams/sources.md)
  All MIDI sources for this connection.
- [var numDestinations: UInt32](midithruconnectionparams/numdestinations.md)
  The number of valid destinations.
- [var destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint)](midithruconnectionparams/destinations.md)
  All MIDI destinations for this connection.
- [var channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](midithruconnectionparams/channelmap.md)
  A mapping of MIDI channels.
- [var filterOutAllControls: UInt8](midithruconnectionparams/filteroutallcontrols.md)
  A value that indicates whether to filter out MIDI continuous control messages.
- [var filterOutBeatClock: UInt8](midithruconnectionparams/filteroutbeatclock.md)
  A value that indicates whether to filter out MIDI clock, play, stop, and resume messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparams/velocity)*