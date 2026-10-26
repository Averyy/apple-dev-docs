# MusicTrackMoveEvents(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Shifts music track events forward or backward in time, in terms of beats.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicTrackMoveEvents(_ inTrack: MusicTrack, _ inStartTime: MusicTimeStamp, _ inEndTime: MusicTimeStamp, _ inMoveTime: MusicTimeStamp) -> OSStatus
```

```c
extern OSStatus MusicTrackMoveEvents(MusicTrack inTrack, MusicTimeStamp inStartTime, MusicTimeStamp inEndTime, MusicTimeStamp inMoveTime);
```

#### Return Value

A result code.

#### Discussion

The `inStartTime` value must be less than the `inEndTime` value.

## Parameters

- `inTrack`: The track whose events you want to move forward or backward in time.
- `inStartTime`: The current start time, in beats, for the music track events you want to move.
- `inEndTime`: The current end time, in beats, for the music track events you want to move.
- `inMoveTime`: The number of beats to move the specified range of music track events. A positive value moves the events toward the end of the music track; a negative value moves the events toward the start.

## See Also

### Managing Music Tracks
- [func MusicTrackClear(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus](./musictrackclear%28_,_,_%29.md)
  Removes a specified range of music track events.
- [func MusicTrackCopyInsert(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus](./musictrackcopyinsert%28_,_,_,_,_%29.md)
  Copies a range of events from one music track and inserts them into another music track.
- [func MusicTrackCut(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus](./musictrackcut%28_,_,_%29.md)
  Removes a specified range of music track events, and shifts later events toward the start of the track to fill in the gap.
- [func MusicTrackGetDestMIDIEndpoint(MusicTrack, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](./musictrackgetdestmidiendpoint%28_,_%29.md)
  Gets the MIDI endpoint that is the event target for a music track.
- [func MusicTrackGetDestNode(MusicTrack, UnsafeMutablePointer<AUNode>) -> OSStatus](./musictrackgetdestnode%28_,_%29.md)
  Gets the audio unit node that is the event target for a music track.
- [func MusicTrackGetProperty(MusicTrack, UInt32, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](./musictrackgetproperty%28_,_,_,_%29.md)
  Gets a music track property value.
- [func MusicTrackGetSequence(MusicTrack, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](./musictrackgetsequence%28_,_%29.md)
  Gets the music sequence that the music track is a member of.
- [func MusicTrackMerge(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus](./musictrackmerge%28_,_,_,_,_%29.md)
  Copies a range of events from one music track and merges them into another music track.
- [func MusicTrackNewAUPresetEvent(MusicTrack, MusicTimeStamp, UnsafePointer<AUPresetEvent>) -> OSStatus](./musictracknewaupresetevent%28_,_,_%29.md)
  Adds an event of type `AUPresetEvent` to a music track.
- [func MusicTrackNewExtendedNoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ExtendedNoteOnEvent>) -> OSStatus](./musictracknewextendednoteevent%28_,_,_%29.md)
  Adds an event of type `ExtendedNoteOnEvent` to a music track.
- [func MusicTrackNewExtendedTempoEvent(MusicTrack, MusicTimeStamp, Float64) -> OSStatus](./musictracknewextendedtempoevent%28_,_,_%29.md)
  Adds a tempo to a music track.
- [func MusicTrackNewMIDIChannelEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIChannelMessage>) -> OSStatus](./musictracknewmidichannelevent%28_,_,_%29.md)
  Adds an event of type `MIDIChannelMessage` to a music track.
- [func MusicTrackNewMIDINoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDINoteMessage>) -> OSStatus](./musictracknewmidinoteevent%28_,_,_%29.md)
  Adds an event of type `MIDINoteMessage` to a music track.
- [func MusicTrackNewMIDIRawDataEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIRawData>) -> OSStatus](./musictracknewmidirawdataevent%28_,_,_%29.md)
  Adds an event of type `MIDIRawData` to a music track.
- [func MusicTrackNewMetaEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIMetaEvent>) -> OSStatus](./musictracknewmetaevent%28_,_,_%29.md)
  Adds an event of type `MIDIMetaEvent` to a music track.
- [NewMusicTrackFrom](./newmusictrackfrom.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musictrackmoveevents(_:_:_:_:))*