# MusicPlayerGetTime(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the playback point for a music player, in beats.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicPlayerGetTime(_ inPlayer: MusicPlayer, _ outTime: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

For converting between beats and seconds, see [`MusicSequenceGetSecondsForBeats(_:_:_:)`](musicsequencegetsecondsforbeats(_:_:_:).md) and [`MusicSequenceGetBeatsForSeconds(_:_:_:)`](musicsequencegetbeatsforseconds(_:_:_:).md).

## Parameters

- `inPlayer`: The music player you want to get the playback point for.
- `outTime`: On output, the playback point for the music player.

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
- [typealias MusicTimeStamp](musictimestamp.md)
  A timestamp for use by a music sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicplayergettime(_:_:))*