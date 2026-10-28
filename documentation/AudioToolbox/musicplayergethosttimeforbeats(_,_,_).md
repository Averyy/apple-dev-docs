# MusicPlayerGetHostTimeForBeats(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets the host time associated with a specified beat.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicPlayerGetHostTimeForBeats(_ inPlayer: MusicPlayer, _ inBeats: MusicTimeStamp, _ outHostTime: UnsafeMutablePointer<UInt64>) -> OSStatus
```

```c
extern OSStatus MusicPlayerGetHostTimeForBeats(MusicPlayer inPlayer, MusicTimeStamp inBeats, UInt64 *outHostTime);
```

## Return Value

A result code. This function returns an error if the player is not playing.

## Discussion

This function is valid only if the music player is playing. For converting between beats and seconds, see [`MusicSequenceGetSecondsForBeats(_:_:_:)`](./musicsequencegetsecondsforbeats%28_,_,_%29.md) and [`MusicSequenceGetBeatsForSeconds(_:_:_:)`](./musicsequencegetbeatsforseconds%28_,_,_%29.md).

## Parameters

- `inPlayer`: The music player that you are querying.
- `inBeats`: The beat number that you want the host time for.
- `outHostTime`: On output, the host time associated with the `inBeats` value.

## See Also

### Managing a Music Player
- [func NewMusicPlayer(UnsafeMutablePointer<MusicPlayer?>) -> OSStatus](./newmusicplayer%28_%29.md)
  Creates a new music player.
- [func DisposeMusicPlayer(MusicPlayer) -> OSStatus](./disposemusicplayer%28_%29.md)
  Disposes of a music player.
- [func MusicPlayerGetBeatsForHostTime(MusicPlayer, UInt64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](./musicplayergetbeatsforhosttime%28_,_,_%29.md)
  Gets the beat number associated a specified host time.
- [func MusicPlayerGetPlayRateScalar(MusicPlayer, UnsafeMutablePointer<Float64>) -> OSStatus](./musicplayergetplayratescalar%28_,_%29.md)
  Gets the playback rate multiplier for a music player.
- [func MusicPlayerGetSequence(MusicPlayer, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](./musicplayergetsequence%28_,_%29.md)
  Gets the music sequence associated with a music player.
- [func MusicPlayerGetTime(MusicPlayer, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](./musicplayergettime%28_,_%29.md)
  Gets the playback point for a music player, in beats.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicplayergethosttimeforbeats(_:_:_:))*