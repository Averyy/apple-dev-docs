# MusicTrackLoopInfo

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

Supports control of the looping behavior of a music track.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MusicTrackLoopInfo
```

```c
typedef struct MusicTrackLoopInfo { ... } MusicTrackLoopInfo;
```

## Overview

This data type is used for the value of the [`kSequenceTrackProperty_LoopInfo`](./ksequencetrackproperty_loopinfo.md) property.

## Topics

### Initializers
- [init()](./musictrackloopinfo/init%28%29.md)
- [init(loopDuration: MusicTimeStamp, numberOfLoops: Int32)](./musictrackloopinfo/init%28loopduration,numberofloops%29.md)
  Initializes the music track loop information.
### Instance Properties
- [var loopDuration: MusicTimeStamp](./musictrackloopinfo/loopduration.md)
  The point in a music track, measured in beats from the end of the music track, at which to begin playback during looped playback.
- [var numberOfLoops: Int32](./musictrackloopinfo/numberofloops.md)
  The number of times to play the designated portion of the music track.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

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
- [func MusicTrackMoveEvents(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTimeStamp) -> OSStatus](./musictrackmoveevents%28_,_,_,_%29.md)
  Shifts music track events forward or backward in time, in terms of beats.
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
- [NewMusicTrackFrom](./newmusictrackfrom.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musictrackloopinfo)*