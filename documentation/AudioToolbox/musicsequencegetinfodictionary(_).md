# MusicSequenceGetInfoDictionary(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Returns a dictionary containing music sequence information.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicSequenceGetInfoDictionary(_ inSequence: MusicSequence) -> CFDictionary
```

#### Return Value

A dictionary object containing information about a music sequence.

#### Discussion

The dictionary can contain one or more of the kAFInfoDictionary_* keys specified in `AudioToolbox/AudioFile.h`. The caller should release the returned dictionary. If the call fails it will return `NULL`

## Parameters

- `inSequence`: The music sequence that you want the information dictionary from.

## See Also

- [func NewMusicSequence(UnsafeMutablePointer<MusicSequence?>) -> OSStatus](newmusicsequence(_:).md)
  Creates a new empty music sequence.
- [func DisposeMusicSequence(MusicSequence) -> OSStatus](disposemusicsequence(_:).md)
  Disposes of a music sequence.
- [func MusicSequenceBarBeatTimeToBeats(MusicSequence, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicsequencebarbeattimetobeats(_:_:_:).md)
  Formats a music sequence’s bar-beat time to its beat time.
- [func MusicSequenceBeatsToBarBeatTime(MusicSequence, MusicTimeStamp, UInt32, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](musicsequencebeatstobarbeattime(_:_:_:_:).md)
  Formats a music sequence’s beat time to its bar-beat time.
- [func MusicSequenceDisposeTrack(MusicSequence, MusicTrack) -> OSStatus](musicsequencedisposetrack(_:_:).md)
  Removes a music track from a music sequence, and disposes of the track.
- [func MusicSequenceFileCreate(MusicSequence, CFURL, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16) -> OSStatus](musicsequencefilecreate(_:_:_:_:_:).md)
  Creates a MIDI file from the events in a music sequence.
- [func MusicSequenceFileCreateData(MusicSequence, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](musicsequencefilecreatedata(_:_:_:_:_:).md)
  Creates a data object containing the events from a music sequence.
- [func MusicSequenceFileLoad(MusicSequence, CFURL, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus](musicsequencefileload(_:_:_:_:).md)
  Loads data into a music sequence from a URL reference.
- [func MusicSequenceFileLoadData(MusicSequence, CFData, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus](musicsequencefileloaddata(_:_:_:_:).md)
  Load data into a music sequence from a data reference.
- [func MusicSequenceGetAUGraph(MusicSequence, UnsafeMutablePointer<AUGraph?>) -> OSStatus](musicsequencegetaugraph(_:_:).md)
  Gets the audio processing graph associated with a music sequence.
- [func MusicSequenceGetBeatsForSeconds(MusicSequence, Float64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicsequencegetbeatsforseconds(_:_:_:).md)
  Calculates the number of beats that correspond to a number of seconds.
- [func MusicSequenceGetIndTrack(MusicSequence, UInt32, UnsafeMutablePointer<MusicTrack?>) -> OSStatus](musicsequencegetindtrack(_:_:_:).md)
  Gets the music track at the specified track index.
- [func MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)](musicsequencegetsmpteresolution(_:_:_:).md)
- [func MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus](musicsequencegetsecondsforbeats(_:_:_:).md)
  Calculates the number of seconds that correspond to a number of beats.
- [func MusicSequenceGetSequenceType(MusicSequence, UnsafeMutablePointer<MusicSequenceType>) -> OSStatus](musicsequencegetsequencetype(_:_:).md)
  Gets the sequence type for a music sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencegetinfodictionary(_:))*