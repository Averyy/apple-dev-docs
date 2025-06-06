# MusicPlayerGetBeatsForHostTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the beat number associated a specified host time.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicPlayerGetBeatsForHostTime(_ inPlayer: MusicPlayer, _ inHostTime: UInt64, _ outBeats: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus
```

#### Return Value

A result code. This function returns an error if the player is not playing.

#### Discussion

This function is valid only if the music player is playing. For converting between beats and seconds, see [`MusicSequenceGetSecondsForBeats(_:_:_:)`](musicsequencegetsecondsforbeats(_:_:_:).md) and [`MusicSequenceGetBeatsForSeconds(_:_:_:)`](musicsequencegetbeatsforseconds(_:_:_:).md).

## Parameters

- `inPlayer`: The music player that you are querying.
- `inHostTime`: The host time that you want the beat number for.
- `outBeats`: On output, the beat number associated with the   value.

## See Also

- [func NewMusicPlayer(UnsafeMutablePointer<MusicPlayer?>) -> OSStatus](newmusicplayer(_:).md)
  Creates a new music player.
- [func DisposeMusicPlayer(MusicPlayer) -> OSStatus](disposemusicplayer(_:).md)
  Disposes of a music player.
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
- [typealias MusicTimeStamp](musictimestamp.md)
  A timestamp for use by a music sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicplayergetbeatsforhosttime(_:_:_:))*