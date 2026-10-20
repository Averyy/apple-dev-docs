# MusicPlayerGetTime(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MusicPlayerGetTime(MusicPlayer inPlayer, MusicTimeStamp *outTime);
```

#### Return Value

A result code.

#### Discussion

For converting between beats and seconds, see [`MusicSequenceGetSecondsForBeats(_:_:_:)`](./musicsequencegetsecondsforbeats%28_,_,_%29.md) and [`MusicSequenceGetBeatsForSeconds(_:_:_:)`](./musicsequencegetbeatsforseconds%28_,_,_%29.md).

## Parameters

- `inPlayer`: The music player you want to get the playback point for.
- `outTime`: On output, the playback point for the music player.

## See Also

### Managing a Music Player
- [func NewMusicPlayer(UnsafeMutablePointer<MusicPlayer?>) -> OSStatus](./newmusicplayer%28_%29.md)
  Creates a new music player.
- [func DisposeMusicPlayer(MusicPlayer) -> OSStatus](./disposemusicplayer%28_%29.md)
  Disposes of a music player.
- [func MusicPlayerGetBeatsForHostTime(MusicPlayer, UInt64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](./musicplayergetbeatsforhosttime%28_,_,_%29.md)
  Gets the beat number associated a specified host time.
- [func MusicPlayerGetHostTimeForBeats(MusicPlayer, MusicTimeStamp, UnsafeMutablePointer<UInt64>) -> OSStatus](./musicplayergethosttimeforbeats%28_,_,_%29.md)
  Gets the host time associated with a specified beat.
- [func MusicPlayerGetPlayRateScalar(MusicPlayer, UnsafeMutablePointer<Float64>) -> OSStatus](./musicplayergetplayratescalar%28_,_%29.md)
  Gets the playback rate multiplier for a music player.
- [func MusicPlayerGetSequence(MusicPlayer, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](./musicplayergetsequence%28_,_%29.md)
  Gets the music sequence associated with a music player.
- [func MusicPlayerIsPlaying(MusicPlayer, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./musicplayerisplaying%28_,_%29.md)
  Indicates whether or not a music player is playing.
- [func MusicPlayerPreroll(MusicPlayer) -> OSStatus](./musicplayerpreroll%28_%29.md)
  Prepares a music player to play.
- [func MusicPlayerSetPlayRateScalar(MusicPlayer, Float64) -> OSStatus](./musicplayersetplayratescalar%28_,_%29.md)
  Sets a playback rate multiplier for a music player.
- [func MusicPlayerSetSequence(MusicPlayer, MusicSequence?) -> OSStatus](./musicplayersetsequence%28_,_%29.md)
  Sets the music sequence for the music player to play.
- [func MusicPlayerSetTime(MusicPlayer, MusicTimeStamp) -> OSStatus](./musicplayersettime%28_,_%29.md)
  Sets the playback point for a music player, in beats.
- [func MusicPlayerStart(MusicPlayer) -> OSStatus](./musicplayerstart%28_%29.md)
  Starts playback of a music player.
- [func MusicPlayerStop(MusicPlayer) -> OSStatus](./musicplayerstop%28_%29.md)
  Stops playback of a music player.
- [typealias MusicPlayer](./musicplayer.md)
  A music player plays a music sequence (of type `MusicSequence`).
- [typealias MusicTimeStamp](./musictimestamp.md)
  A timestamp for use by a music sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicplayergettime(_:_:))*