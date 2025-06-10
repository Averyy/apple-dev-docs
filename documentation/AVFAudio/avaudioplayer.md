# AVAudioPlayer

**Framework**: AVFAudio  
**Kind**: class

An object that plays audio data from a file or buffer.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class AVAudioPlayer
```

#### Overview

Use an audio player to:

- Play audio of any duration from a file or buffer
- Control the volume, panning, rate, and looping behavior of the played audio
- Access playback-level metering data
- Play multiple sounds simultaneously by synchronizing the playback of multiple players

For more information about preparing your app to play audio, see [`Configuring your app for media playback`](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback).

> ❗ **Important**:  For more advanced playback capabilities, like playing streaming or positional audio, use [`AVAudioEngine`](avaudioengine.md) instead.

## Topics

### Creating an audio player
- [init(contentsOf: URL) throws](avaudioplayer/init(contentsof:).md)
  Creates a player to play audio from a file.
- [init(contentsOf: URL, fileTypeHint: String?) throws](avaudioplayer/init(contentsof:filetypehint:).md)
  Creates a player to play audio from a file of a particular type.
- [init(data: Data) throws](avaudioplayer/init(data:).md)
  Creates a player to play in-memory audio data.
- [init(data: Data, fileTypeHint: String?) throws](avaudioplayer/init(data:filetypehint:).md)
  Creates a player to play in-memory audio data of a particular type.
### Controlling playback
- [func prepareToPlay() -> Bool](avaudioplayer/preparetoplay.md)
  Prepares the player for audio playback.
- [func play() -> Bool](avaudioplayer/play.md)
  Plays audio asynchronously.
- [func play(atTime: TimeInterval) -> Bool](avaudioplayer/play(attime:).md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func pause()](avaudioplayer/pause.md)
  Pauses audio playback.
- [func stop()](avaudioplayer/stop.md)
  Stops playback and undoes the setup the system requires for playback.
- [var isPlaying: Bool](avaudioplayer/isplaying.md)
  A Boolean value that indicates whether the player is currently playing audio.
### Configuring playback settings
- [var volume: Float](avaudioplayer/volume.md)
  The audio player’s volume relative to other audio output.
- [func setVolume(Float, fadeDuration: TimeInterval)](avaudioplayer/setvolume(_:fadeduration:).md)
  Changes the audio player’s volume over a duration of time.
- [var pan: Float](avaudioplayer/pan.md)
  The audio player’s stereo pan position.
- [var enableRate: Bool](avaudioplayer/enablerate.md)
  A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [var rate: Float](avaudioplayer/rate.md)
  The audio player’s playback rate.
- [var numberOfLoops: Int](avaudioplayer/numberofloops.md)
  The number of times the audio repeats playback.
### Accessing player timing
- [var currentTime: TimeInterval](avaudioplayer/currenttime.md)
  The current playback time, in seconds, within the audio timeline.
- [var duration: TimeInterval](avaudioplayer/duration.md)
  The total duration, in seconds, of the player’s audio.
### Managing audio channels
- [var numberOfChannels: Int](avaudioplayer/numberofchannels.md)
  The number of audio channels in the player’s audio.
- [var channelAssignments: [AVAudioSessionChannelDescription]?](avaudioplayer/channelassignments.md)
  An array of channel descriptions for the audio player.
### Managing audio-level metering
- [var isMeteringEnabled: Bool](avaudioplayer/ismeteringenabled.md)
  A Boolean value that indicates whether the player is able to generate audio-level metering data.
- [func updateMeters()](avaudioplayer/updatemeters.md)
  Refreshes the average and peak power values for all channels of an audio player.
- [func averagePower(forChannel: Int) -> Float](avaudioplayer/averagepower(forchannel:).md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [func peakPower(forChannel: Int) -> Float](avaudioplayer/peakpower(forchannel:).md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.
### Responding to player events
- [var delegate: (any AVAudioPlayerDelegate)?](avaudioplayer/delegate.md)
  The delegate object for the audio player.
- [protocol AVAudioPlayerDelegate](avaudioplayerdelegate.md)
  A protocol that defines the methods to respond to audio playback events and decoding errors.
### Inspecting the audio data
- [var url: URL?](avaudioplayer/url.md)
  The URL of the audio file.
- [var data: Data?](avaudioplayer/data.md)
  The audio data associated with the player.
- [var format: AVAudioFormat](avaudioplayer/format.md)
  The format of the player’s audio data.
- [var settings: [String : Any]](avaudioplayer/settings.md)
  A dictionary that provides information about the player’s audio data.
### Accessing device information
- [var currentDevice: String?](avaudioplayer/currentdevice.md)
  The unique identifier of the current audio player.
- [var deviceCurrentTime: TimeInterval](avaudioplayer/devicecurrenttime.md)
  The time value, in seconds, of the audio output device’s clock.
### Instance Properties
- [var intendedSpatialExperience: any SpatialAudioExperience](avaudioplayer/intendedspatialexperience-27klj.md)
  The AVAudioPlayer’s intended spatial experience.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioRecorder](avaudiorecorder.md)
  An object that records audio data to a file.
- [class AVMIDIPlayer](avmidiplayer.md)
  An object that plays MIDI data through a system sound module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer)*