# MIDIThruConnectionParams

**Framework**: Core MIDI  
**Kind**: struct

A set of MIDI routings and transformations.

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
struct MIDIThruConnectionParams
```

## Topics

### Connection Parameters
- [var noteNumber: MIDITransform](midithruconnectionparams/notenumber.md)
  The transformation of MIDI note numbers.
- [var lowNote: UInt8](midithruconnectionparams/lownote.md)
  The note value below which the system filters out notes.
- [var highNote: UInt8](midithruconnectionparams/highnote.md)
  The note value above which the system filters out notes.
- [var velocity: MIDITransform](midithruconnectionparams/velocity.md)
  A note velocity transformation.
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
- [var filterOutMTC: UInt8](midithruconnectionparams/filteroutmtc.md)
  A value that indicates whether to filter out MIDI Time Code messages.
- [var filterOutSysEx: UInt8](midithruconnectionparams/filteroutsysex.md)
  A value that indicates wheter to filter out system-exclusive messages.
- [var filterOutTuneRequest: UInt8](midithruconnectionparams/filterouttunerequest.md)
  A value that specifies whether to filter out MIDI tune request messages.
- [var numControlTransforms: UInt16](midithruconnectionparams/numcontroltransforms.md)
  The number of control transformations in the variable-length portion of the struct.
- [var numMaps: UInt16](midithruconnectionparams/nummaps.md)
  The number of MIDI value maps in the variable-length portion of the struct.
- [var pitchBend: MIDITransform](midithruconnectionparams/pitchbend.md)
  The transformation of a MIDI pitch bend event.
- [var programChange: MIDITransform](midithruconnectionparams/programchange.md)
  A transformation of a MIDI program change event.
- [var reserved2: (UInt8, UInt8, UInt8)](midithruconnectionparams/reserved2.md)
  A reserved value that must be 0.
- [var reserved3: (UInt16, UInt16, UInt16, UInt16)](midithruconnectionparams/reserved3.md)
  A reserved value that must be 0.
### Initializers
- [init()](midithruconnectionparams/init.md)
- [init(version: UInt32, numSources: UInt32, sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), numDestinations: UInt32, destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), lowVelocity: UInt8, highVelocity: UInt8, lowNote: UInt8, highNote: UInt8, noteNumber: MIDITransform, velocity: MIDITransform, keyPressure: MIDITransform, channelPressure: MIDITransform, programChange: MIDITransform, pitchBend: MIDITransform, filterOutSysEx: UInt8, filterOutMTC: UInt8, filterOutBeatClock: UInt8, filterOutTuneRequest: UInt8, reserved2: (UInt8, UInt8, UInt8), filterOutAllControls: UInt8, numControlTransforms: UInt16, numMaps: UInt16, reserved3: (UInt16, UInt16, UInt16, UInt16))](midithruconnectionparams/init(version:numsources:sources:numdestinations:destinations:channelmap:lowvelocity:highvelocity:lownote:highnote:notenumber:velocity:keypressure:channelpressure:programchange:pitchbend:filteroutsysex:filteroutmtc:filteroutbeatclock:filtero-6y1ig.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func MIDIThruConnectionParamsSize(UnsafePointer<MIDIThruConnectionParams>) -> Int](midithruconnectionparamssize(_:).md)
  Returns the size of a MIDI thru connection parameters object.
- [func MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)](midithruconnectionparamsinitialize(_:).md)
  Initializes a parameters object with its default values.
- [func MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](midithruconnectiongetparams(_:_:).md)
  Returns the thru connection’s parameters.
- [func MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData) -> OSStatus](midithruconnectionsetparams(_:_:).md)
  Updates a thru connection’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparams)*