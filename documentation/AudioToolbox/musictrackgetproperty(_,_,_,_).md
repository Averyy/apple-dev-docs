# MusicTrackGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets a music track property value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicTrackGetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ outData: UnsafeMutableRawPointer, _ ioLength: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus MusicTrackGetProperty(MusicTrack inTrack, UInt32 inPropertyID, void *outData, UInt32 *ioLength);
```

## Return Value

A result code.

## Discussion

Music track property values are always accessed by reference. As of OS X v10.6, all such property values are fixed length.

This function’s main purpose is to retrieve a music track property value, but you also use it to obtain the size of a variable-length property. Do this, prior to retrieving a variable-length property value, to ensure that you allocate enough memory in `outData` to hold the value.

To obtain a property value’s size, call this function with the `outData` parameter set to `NULL`. On output, the `ioLength` parameter contains the property size.

## Parameters

- `inTrack`: The music track that you want to get a property value from.
- `inPropertyID`: The identifier for the music track property that you want to get. See [Music Track Properties](./api-1515456-music-track-properties.md) for possible values.
- `outData`: On output, the requested property value.
- `ioLength`: On input, the available size for the retrieved property value. On output, the size of the valid property data that `outData` points to.

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
- [func MusicTrackNewMetaEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIMetaEvent>) -> OSStatus](./musictracknewmetaevent%28_,_,_%29.md)
  Adds an event of type `MIDIMetaEvent` to a music track.
- [NewMusicTrackFrom](./newmusictrackfrom.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musictrackgetproperty(_:_:_:_:))*