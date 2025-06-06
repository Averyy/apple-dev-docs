# MusicSequenceSetUserCallback(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Registers a user callback function with a music sequence.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: MusicSequenceUserCallback?, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

The music sequence invokes your callback for each user event added to any music track owned by the sequence. If there is a callback registered, then UserEvents will be chased when MusicPlayerSetTime is called. In that case the inStartSliceBeat and inEndSliceBeat will both be the same value and will be the beat that the player is chasing to.

Usually, where the sequence data is being scheduled for playback, the following applies:

```objc
inStartSliceBeat <= inEventTime < inEndSliceBeat
```

The only exception to this is if the track that owns the MusicEvent is looping. In this case the start beat will still be less than the end beat (so your callback can still determine that it is playing, and what beats are currently being scheduled), however, the inEventTime will be the original time-stamped time of the user event.

## Parameters

- `inSequence`: The music sequence that you want to add a user callback function to.
- `inCallback`: A reference to your callback function. Use   to remove a registered callback function.
- `inClientData`: Your data that the music sequence provides back to your callback function when it is invoked.

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
- [func MusicSequenceGetInfoDictionary(MusicSequence) -> CFDictionary](musicsequencegetinfodictionary(_:).md)
  Returns a dictionary containing music sequence information.
- [func MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)](musicsequencegetsmpteresolution(_:_:_:).md)
- [func MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus](musicsequencegetsecondsforbeats(_:_:_:).md)
  Calculates the number of seconds that correspond to a number of beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencesetusercallback(_:_:_:))*