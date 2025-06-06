# MIDIMetaEvent

**Framework**: Audio Toolbox  
**Kind**: struct

Describes a MIDI metaevent such as lyric text, time signature, and so on.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MIDIMetaEvent
```

## Topics

### Initializers
- [init()](midimetaevent/init.md)
- [init(metaEventType: UInt8, unused1: UInt8, unused2: UInt8, unused3: UInt8, dataLength: UInt32, data: UInt8)](midimetaevent/init(metaeventtype:unused1:unused2:unused3:datalength:data:).md)
### Instance Properties
- [var data: UInt8](midimetaevent/data.md)
- [var dataLength: UInt32](midimetaevent/datalength.md)
- [var metaEventType: UInt8](midimetaevent/metaeventtype.md)
  An integer that designates one of the types of MIDI metaevents.
- [var unused1: UInt8](midimetaevent/unused1.md)
- [var unused2: UInt8](midimetaevent/unused2.md)
- [var unused3: UInt8](midimetaevent/unused3.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func MusicTrackClear(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus](musictrackclear(_:_:_:).md)
  Removes a specified range of music track events.
- [func MusicTrackCopyInsert(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus](musictrackcopyinsert(_:_:_:_:_:).md)
  Copies a range of events from one music track and inserts them into another music track.
- [func MusicTrackCut(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus](musictrackcut(_:_:_:).md)
  Removes a specified range of music track events, and shifts later events toward the start of the track to fill in the gap.
- [func MusicTrackGetDestMIDIEndpoint(MusicTrack, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](musictrackgetdestmidiendpoint(_:_:).md)
  Gets the MIDI endpoint that is the event target for a music track.
- [func MusicTrackGetDestNode(MusicTrack, UnsafeMutablePointer<AUNode>) -> OSStatus](musictrackgetdestnode(_:_:).md)
  Gets the audio unit node that is the event target for a music track.
- [func MusicTrackGetProperty(MusicTrack, UInt32, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](musictrackgetproperty(_:_:_:_:).md)
  Gets a music track property value.
- [func MusicTrackGetSequence(MusicTrack, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](musictrackgetsequence(_:_:).md)
  Gets the music sequence that the music track is a member of.
- [func MusicTrackMerge(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus](musictrackmerge(_:_:_:_:_:).md)
  Copies a range of events from one music track and merges them into another music track.
- [func MusicTrackMoveEvents(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTimeStamp) -> OSStatus](musictrackmoveevents(_:_:_:_:).md)
  Shifts music track events forward or backward in time, in terms of beats.
- [func MusicTrackNewAUPresetEvent(MusicTrack, MusicTimeStamp, UnsafePointer<AUPresetEvent>) -> OSStatus](musictracknewaupresetevent(_:_:_:).md)
  Adds an event of type `AUPresetEvent` to a music track.
- [func MusicTrackNewExtendedNoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ExtendedNoteOnEvent>) -> OSStatus](musictracknewextendednoteevent(_:_:_:).md)
  Adds an event of type `ExtendedNoteOnEvent` to a music track.
- [func MusicTrackNewExtendedTempoEvent(MusicTrack, MusicTimeStamp, Float64) -> OSStatus](musictracknewextendedtempoevent(_:_:_:).md)
  Adds a tempo to a music track.
- [func MusicTrackNewMIDIChannelEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIChannelMessage>) -> OSStatus](musictracknewmidichannelevent(_:_:_:).md)
  Adds an event of type `MIDIChannelMessage` to a music track.
- [func MusicTrackNewMIDINoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDINoteMessage>) -> OSStatus](musictracknewmidinoteevent(_:_:_:).md)
  Adds an event of type `MIDINoteMessage` to a music track.
- [func MusicTrackNewMIDIRawDataEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIRawData>) -> OSStatus](musictracknewmidirawdataevent(_:_:_:).md)
  Adds an event of type `MIDIRawData` to a music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/midimetaevent)*