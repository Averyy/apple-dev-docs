# MusicSequenceFileCreate(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a MIDI file from the events in a music sequence.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicSequenceFileCreate(_ inSequence: MusicSequence, _ inFileRef: CFURL, _ inFileType: MusicSequenceFileTypeID, _ inFlags: MusicSequenceFileFlags, _ inResolution: Int16) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

This function can be (and is most commonly) used to create a MIDI file from the events in a sequence. Only MIDI based events are used when creating the MIDI file. MIDI files are normally beat based, but can also have a SMPTE (or real-time rather than beat time) representation.

The inResolution parameter specifies the relationship between “tick” and quarter note for saving to a standard MIDI file. Pass 0 to this parameter to use the default value; namely, the value that is currently set on the tempo track.

The various sequence types determine the kinds of files that can be created, as follows:

- Beats—When saving a MIDI file, it saves a beats (PPQ) based axis.
- Seconds—When saving a MIDI file, it will save it as a SMPTE resolution - so you should specify this resolution when creating the MIDI file. If zero is specified, 25 fps and 40 ticks/frame is used (a time scale of a millisecond)
- Samples—You cannot save to a MIDI file with this sequence type.

The complete meaning of the 16-bit “division” field in a MIDI File’s MThd chunk. If it is positive, then a tick represents 1/D quarter notes.  If it negative, the following pertains:

- Bits 14-8 are a signed 7-bit number representing the SMPTE format: 24, -25, -29 (drop), -30.
- Bits 7-0 represents the number of ticks per SMPTE frame. Typical values are 4, 10, 80, 100. You can obtain millisecond resolution by specifying 25 frames/sec and 40 divisions/frame:

```objc
  30 fps with 80 bits (ticks) per frame: 0xE250  ((char)0xE2 == -30)
```

## Parameters

- `inSequence`: The music sequence that you want to create a MIDI file from.
- `inFileRef`: The URL to the MIDI file to be created.
- `inFileType`: The type of file to create.
- `inFlags`: Flags that configure the file creation process.
- `inResolution`: The resolution, which depends on the file type and the music sequence type.

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
- [func MusicSequenceGetInfoDictionary(MusicSequence) -> CFDictionary](musicsequencegetinfodictionary(_:).md)
  Returns a dictionary containing music sequence information.
- [func MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)](musicsequencegetsmpteresolution(_:_:_:).md)
- [func MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus](musicsequencegetsecondsforbeats(_:_:_:).md)
  Calculates the number of seconds that correspond to a number of beats.
- [func MusicSequenceGetSequenceType(MusicSequence, UnsafeMutablePointer<MusicSequenceType>) -> OSStatus](musicsequencegetsequencetype(_:_:).md)
  Gets the sequence type for a music sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencefilecreate(_:_:_:_:_:))*