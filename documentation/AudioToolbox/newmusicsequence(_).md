# NewMusicSequence(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Creates a new empty music sequence.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func NewMusicSequence(_ outSequence: UnsafeMutablePointer<MusicSequence?>) -> OSStatus
```

```c
extern OSStatus NewMusicSequence(MusicSequence*outSequence);
```

## Return Value

A result code.

## Discussion

A new music sequence has only a tempo track, with a default tempo of 120 beats-per-minute. The default sequence type is beat-based. For the various sequence types, see [`MusicSequenceType`](./musicsequencetype.md).

To direct the output of a music sequence to an audio processing graph, use the [`MusicSequenceSetAUGraph(_:_:)`](./musicsequencesetaugraph%28_,_%29.md) function. To direct the output instead to a MIDI endpoint, use the [`MusicSequenceSetMIDIEndpoint(_:_:)`](./musicsequencesetmidiendpoint%28_,_%29.md) function.

To direct the output of a specific music track, use the [`MusicTrackSetDestNode(_:_:)`](./musictracksetdestnode%28_,_%29.md) and [`MusicTrackSetDestMIDIEndpoint(_:_:)`](./musictracksetdestmidiendpoint%28_,_%29.md) functions, described in `MusicTrack`.

## Parameters

- `outSequence`: On output, the new, empty music sequence.

## See Also

### Managing Music Sequences
- [func DisposeMusicSequence(MusicSequence) -> OSStatus](./disposemusicsequence%28_%29.md)
  Disposes of a music sequence.
- [func MusicSequenceBarBeatTimeToBeats(MusicSequence, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](./musicsequencebarbeattimetobeats%28_,_,_%29.md)
  Formats a music sequence’s bar-beat time to its beat time.
- [func MusicSequenceBeatsToBarBeatTime(MusicSequence, MusicTimeStamp, UInt32, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](./musicsequencebeatstobarbeattime%28_,_,_,_%29.md)
  Formats a music sequence’s beat time to its bar-beat time.
- [func MusicSequenceDisposeTrack(MusicSequence, MusicTrack) -> OSStatus](./musicsequencedisposetrack%28_,_%29.md)
  Removes a music track from a music sequence, and disposes of the track.
- [func MusicSequenceFileCreate(MusicSequence, CFURL, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16) -> OSStatus](./musicsequencefilecreate%28_,_,_,_,_%29.md)
  Creates a MIDI file from the events in a music sequence.
- [func MusicSequenceFileCreateData(MusicSequence, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](./musicsequencefilecreatedata%28_,_,_,_,_%29.md)
  Creates a data object containing the events from a music sequence.
- [func MusicSequenceFileLoad(MusicSequence, CFURL, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus](./musicsequencefileload%28_,_,_,_%29.md)
  Loads data into a music sequence from a URL reference.
- [func MusicSequenceFileLoadData(MusicSequence, CFData, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus](./musicsequencefileloaddata%28_,_,_,_%29.md)
  Load data into a music sequence from a data reference.
- [func MusicSequenceGetAUGraph(MusicSequence, UnsafeMutablePointer<AUGraph?>) -> OSStatus](./musicsequencegetaugraph%28_,_%29.md)
  Gets the audio processing graph associated with a music sequence.
- [func MusicSequenceGetBeatsForSeconds(MusicSequence, Float64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](./musicsequencegetbeatsforseconds%28_,_,_%29.md)
  Calculates the number of beats that correspond to a number of seconds.
- [func MusicSequenceGetIndTrack(MusicSequence, UInt32, UnsafeMutablePointer<MusicTrack?>) -> OSStatus](./musicsequencegetindtrack%28_,_,_%29.md)
  Gets the music track at the specified track index.
- [func MusicSequenceGetInfoDictionary(MusicSequence) -> CFDictionary](./musicsequencegetinfodictionary%28_%29.md)
  Returns a dictionary containing music sequence information.
- [func MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)](./musicsequencegetsmpteresolution%28_,_,_%29.md)
- [func MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus](./musicsequencegetsecondsforbeats%28_,_,_%29.md)
  Calculates the number of seconds that correspond to a number of beats.
- [func MusicSequenceGetSequenceType(MusicSequence, UnsafeMutablePointer<MusicSequenceType>) -> OSStatus](./musicsequencegetsequencetype%28_,_%29.md)
  Gets the sequence type for a music sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/newmusicsequence(_:))*