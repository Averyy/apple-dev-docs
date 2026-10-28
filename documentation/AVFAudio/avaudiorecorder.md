# AVAudioRecorder

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that records audio data to a file.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class AVAudioRecorder
```

```objc
@interface AVAudioRecorder : NSObject
```

## Mentions

- [Routing audio to specific devices in multidevice sessions](./routing-audio-to-specific-devices-in-multidevice-sessions.md)

## Overview

Use an audio recorder to:

- Record audio from the system’s active input device
- Record for a specified duration or until the user stops recording
- Pause and resume a recording
- Access recording-level metering data

To record audio in iOS or tvOS, configure your audio session to use the [`record`](./avaudiosession/category-swift.struct/record.md) or [`playAndRecord`](./avaudiosession/category-swift.struct/playandrecord.md) category.

> ❗ **Important**:  For more advanced recording capabilities, like applying signal processing to recorded audio, use [`AVAudioEngine`](./avaudioengine.md) instead.

## Topics

### Creating an audio recorder
- [init(url: URL, settings: [String : Any]) throws](./avaudiorecorder/init%28url,settings%29-5whyq.md)
  Creates an audio recorder with settings.
- [init(url: URL, format: AVAudioFormat) throws](./avaudiorecorder/init%28url,format%29-7herw.md)
  Creates an audio recorder with an audio format.
### Controlling recording
- [func prepareToRecord() -> Bool](./avaudiorecorder/preparetorecord%28%29.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](./avaudiorecorder/record%28%29.md)
  Starts or resumes audio recording.
- [func record(atTime: TimeInterval) -> Bool](./avaudiorecorder/record%28attime%29.md)
  Records audio starting at a specific time.
- [func record(forDuration: TimeInterval) -> Bool](./avaudiorecorder/record%28forduration%29.md)
  Records audio for the indicated duration of time.
- [func record(atTime: TimeInterval, forDuration: TimeInterval) -> Bool](./avaudiorecorder/record%28attime,forduration%29.md)
  Records audio starting at a specific time for the indicated duration.
- [func pause()](./avaudiorecorder/pause%28%29.md)
  Pauses an audio recording.
- [func stop()](./avaudiorecorder/stop%28%29.md)
  Stops recording and closes the audio file.
- [var isRecording: Bool](./avaudiorecorder/isrecording.md)
  A Boolean value that indicates whether the audio recorder is recording.
- [func deleteRecording() -> Bool](./avaudiorecorder/deleterecording%28%29.md)
  Deletes a recorded audio file.
### Accessing recorder timing
- [var currentTime: TimeInterval](./avaudiorecorder/currenttime.md)
  The time, in seconds, since the beginning of the recording.
- [var deviceCurrentTime: TimeInterval](./avaudiorecorder/devicecurrenttime.md)
  The time, in seconds, of the host audio device.
### Managing audio channels
- [var channelAssignments: [AVAudioSessionChannelDescription]?](./avaudiorecorder/channelassignments.md)
  An array of channel descriptions associated with the audio recorder.
### Managing audio-level metering
- [var isMeteringEnabled: Bool](./avaudiorecorder/ismeteringenabled.md)
  A Boolean value that indicates whether you’ve enabled the recorder to generate audio-level metering data.
- [func updateMeters()](./avaudiorecorder/updatemeters%28%29.md)
  Refreshes the average and peak power values for all channels of an audio recorder.
- [func averagePower(forChannel: Int) -> Float](./avaudiorecorder/averagepower%28forchannel%29.md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [func peakPower(forChannel: Int) -> Float](./avaudiorecorder/peakpower%28forchannel%29.md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.
### Responding to recorder events
- [var delegate: (any AVAudioRecorderDelegate)?](./avaudiorecorder/delegate.md)
  The delegate object for the audio recorder.
- [protocol AVAudioRecorderDelegate](./avaudiorecorderdelegate.md)
  A protocol that defines the methods to respond to audio recording events and encoding errors.
### Inspecting the audio data
- [var url: URL](./avaudiorecorder/url.md)
  The URL to which the recorder writes its data.
- [var format: AVAudioFormat](./avaudiorecorder/format.md)
  The format of the recorded audio.
- [var settings: [String : Any]](./avaudiorecorder/settings.md)
  The settings that describe the format of the recorded audio.
### Initializers
- [init(URL: URL, format: AVAudioFormat) throws](./avaudiorecorder/init%28url,format%29-hpsc.md)
- [init(URL: URL, settings: [String : Any]) throws](./avaudiorecorder/init%28url,settings%29-9zay9.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Basic playback and recording
- [class AVAudioPlayer](./avaudioplayer.md)
  An object that plays audio data from a file or buffer.
- [class AVMIDIPlayer](./avmidiplayer.md)
  An object that plays MIDI data through a system sound module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder)*