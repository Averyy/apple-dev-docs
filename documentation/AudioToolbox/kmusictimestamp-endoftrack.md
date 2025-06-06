# kMusicTimeStamp_EndOfTrack

**Framework**: Audio Toolbox  
**Kind**: var

Indicates a time immediately beyond the last music event in a music track. Use this value when selecting all music events starting at a designated time and extending to, and including, the last event in a track. Also use this value to position an iterator for moving backward through a track, from the end to the start. See also [`NewMusicEventIterator(_:_:)`](newmusiceventiterator(_:_:).md) and [`MusicEventIteratorSeek(_:_:)`](musiceventiteratorseek(_:_:).md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kMusicTimeStamp_EndOfTrack: Double { get }
```

## See Also

- [func NewMusicPlayer(UnsafeMutablePointer<MusicPlayer?>) -> OSStatus](newmusicplayer(_:).md)
  Creates a new music player.
- [func DisposeMusicPlayer(MusicPlayer) -> OSStatus](disposemusicplayer(_:).md)
  Disposes of a music player.
- [func MusicPlayerGetBeatsForHostTime(MusicPlayer, UInt64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicplayergetbeatsforhosttime(_:_:_:).md)
  Gets the beat number associated a specified host time.
- [func MusicPlayerGetHostTimeForBeats(MusicPlayer, MusicTimeStamp, UnsafeMutablePointer<UInt64>) -> OSStatus](musicplayergethosttimeforbeats(_:_:_:).md)
  Gets the host time associated with a specified beat.
- [func MusicPlayerGetPlayRateScalar(MusicPlayer, UnsafeMutablePointer<Float64>) -> OSStatus](musicplayergetplayratescalar(_:_:).md)
  Gets the playback rate multiplier for a music player.
- [func MusicPlayerGetSequence(MusicPlayer, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](musicplayergetsequence(_:_:).md)
  Gets the music sequence associated with a music player.
- [func MusicPlayerGetTime(MusicPlayer, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicplayergettime(_:_:).md)
  Gets the playback point for a music player, in beats.
- [func MusicPlayerIsPlaying(MusicPlayer, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](musicplayerisplaying(_:_:).md)
  Indicates whether or not a music player is playing.
- [func MusicPlayerPreroll(MusicPlayer) -> OSStatus](musicplayerpreroll(_:).md)
  Prepares a music player to play.
- [func MusicPlayerSetPlayRateScalar(MusicPlayer, Float64) -> OSStatus](musicplayersetplayratescalar(_:_:).md)
  Sets a playback rate multiplier for a music player.
- [func MusicPlayerSetSequence(MusicPlayer, MusicSequence?) -> OSStatus](musicplayersetsequence(_:_:).md)
  Sets the music sequence for the music player to play.
- [func MusicPlayerSetTime(MusicPlayer, MusicTimeStamp) -> OSStatus](musicplayersettime(_:_:).md)
  Sets the playback point for a music player, in beats.
- [func MusicPlayerStart(MusicPlayer) -> OSStatus](musicplayerstart(_:).md)
  Starts playback of a music player.
- [func MusicPlayerStop(MusicPlayer) -> OSStatus](musicplayerstop(_:).md)
  Stops playback of a music player.
- [typealias MusicPlayer](musicplayer.md)
  A music player plays a music sequence (of type `MusicSequence`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kmusictimestamp_endoftrack)*