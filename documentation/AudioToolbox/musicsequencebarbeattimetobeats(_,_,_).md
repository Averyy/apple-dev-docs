# MusicSequenceBarBeatTimeToBeats(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Formats a music sequence’s bar-beat time to its beat time.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicSequenceBarBeatTimeToBeats(_ inSequence: MusicSequence, _ inBarBeatTime: UnsafePointer<CABarBeatTime>, _ outBeats: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus
```

```c
extern OSStatus MusicSequenceBarBeatTimeToBeats(MusicSequence inSequence, const CABarBeatTime *inBarBeatTime, MusicTimeStamp *outBeats);
```

## Return Value

A result code.

## Discussion

The sequence’s tempo track time signature events are used to to calculate the bar-beat representation. If there are no Time Sig events added to the sequence 4/4 is assumed. A time signature event is a MIDI Meta Event as specified for MIDI files.

Refer to `AudioToolbox/CAClock.h` for more information.

## Parameters

- `inSequence`: The music sequence that you want the beat count for.
- `inBarBeatTime`: The bar-beat time to be represented as beats.
- `outBeats`: On output, the music sequence’s beat time.

## See Also

### Managing Music Sequences
- [func NewMusicSequence(UnsafeMutablePointer<MusicSequence?>) -> OSStatus](./newmusicsequence%28_%29.md)
  Creates a new empty music sequence.
- [func DisposeMusicSequence(MusicSequence) -> OSStatus](./disposemusicsequence%28_%29.md)
  Disposes of a music sequence.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencebarbeattimetobeats(_:_:_:))*