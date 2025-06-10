# AVAudioPlayerNode

**Framework**: AVFAudio  
**Kind**: class

An object for scheduling the playback of buffers or segments of audio files.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioPlayerNode
```

#### Overview

This audio node supports scheduling the playback of [`AVAudioPCMBuffer`](avaudiopcmbuffer.md) instances, or segments of audio files that you open through [`AVAudioFile`](avaudiofile.md). You can schedule buffers and segments to play at specific points in time or to play immediately following preceding segments.

Generally, you want to configure the node’s output format with the same number of channels as in the files and buffers. Otherwise, the node drops or adds channels as necessary. It’s usually preferable to use an [`AVAudioMixerNode`](avaudiomixernode.md) for this configuration.

Similarly, when playing file segments, the node makes sample rate conversions, if necessary. It’s preferable to configure the node’s output sample rate to match that of the files, and to use a mixer to perform the rate conversion.

When playing buffers, there’s an implicit assumption that the buffers are at the same sample rate as the node’s output format.

The [`stop()`](avaudioplayernode/stop().md) method unschedules all previously scheduled buffers and file segments, and returns the player timeline to sample time `0`.

> **Note**:  The `AVAudioPlayerNode` class isn’t key-value observing compliant, and may indicate that Combine publishers are available. Don’t use them for monitoring changes.

##### Player Timeline

The usual [`AVAudioNode`](avaudionode.md) sample times, which [`lastRenderTime`](avaudionode/lastrendertime.md) observes, have an arbitrary zero point. The `AVAudioPlayerNode` class superimposes a second player timeline on top of this to reflect when the player starts and intervals when it pauses. The methods [`nodeTime(forPlayerTime:)`](avaudioplayernode/nodetime(forplayertime:).md) and [`playerTime(forNodeTime:)`](avaudioplayernode/playertime(fornodetime:).md) convert between the two.

##### Scheduling Playback Time

The [`scheduleBuffer(_:at:options:completionHandler:)`](avaudioplayernode/schedulebuffer(_:at:options:completionhandler:).md), [`scheduleFile(_:at:completionHandler:)`](avaudioplayernode/schedulefile(_:at:completionhandler:).md), and [`scheduleSegment(_:startingFrame:frameCount:at:completionHandler:)`](avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completionhandler:).md) methods take an [`AVAudioTime`](avaudiotime.md) `when` parameter, and you interpret it as follows:

- If the `when` parameter is `nil`:
- If there are previous commands, the new one plays immediately following the last one.
- Otherwise, if the node is in a playing state, the event plays in the very near future.
- Otherwise, the command plays at sample time `0`.
- If the `when` parameter is a sample time, the parameter interprets it as such.
- If the `when` parameter is a host time, the system ignores it unless the sample time is invalid when the engine is rendering to an audio device.

The scheduling methods fail if:

- A buffer’s channel count doesn’t match that of the node’s output format.
- The system can’t access a file.
- An [`AVAudioTime`](avaudiotime.md) doesn’t specify a valid sample time or a host time.
- A segment’s start frame or frame count is a negative value.

##### Handling Buffer or File Completion

The buffer of file completion handlers are a means to schedule more data if available on the player node. For more information on the different completion callback types, see [`AVAudioPlayerNodeCompletionCallbackType`](avaudioplayernodecompletioncallbacktype.md).

> ❗ **Important**:  Don’t stop a player within a completion handler callback because it can deadlock while trying to unschedule already scheduled buffers.

##### Rendering Offline

When you use a player node with the engine operating in manual rendering mode, you use the buffer or file completion handlers — [`lastRenderTime`](avaudionode/lastrendertime.md), [`latency`](avaudionode/latency.md), and [`outputPresentationLatency`](avaudionode/outputpresentationlatency.md) — to track how much data the player rendered and how much remains to render.

## Topics

### Creating a Player Node
- [init()](avaudioplayernode/init.md)
  Creates an initialized audio player node.
### Scheduling Playback
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionHandler: (() -> Void)?)](avaudioplayernode/schedulefile(_:at:completionhandler:).md)
  Schedules the playing of an entire audio file.
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulefile(_:at:completioncallbacktype:completionhandler:).md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionHandler: (() -> Void)?)](avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completionhandler:).md)
  Schedules the playing of an audio file segment.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulesegment(_:startingframe:framecount:at:completioncallbacktype:completionhandler:).md)
  Schedules the playing of an audio file segment with a callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:at:options:completionhandler:).md)
  Schedules the playing samples from an audio buffer at the time and playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](avaudioplayernode/schedulebuffer(_:completionhandler:).md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulebuffer(_:at:options:completioncallbacktype:completionhandler:).md)
  Schedules the playing samples from an audio buffer with the playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](avaudioplayernode/schedulebuffer(_:completioncallbacktype:completionhandler:).md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [struct AVAudioPlayerNodeBufferOptions](avaudioplayernodebufferoptions.md)
  The buffer options that control the playback scheduling.
- [enum AVAudioPlayerNodeCompletionCallbackType](avaudioplayernodecompletioncallbacktype.md)
  Constants that specify when the framework must invoke the completion handler.
- [typealias AVAudioPlayerNodeCompletionHandler](avaudioplayernodecompletionhandler.md)
  The callback handler for buffer or file completion.
### Converting Node and Player Times
- [func nodeTime(forPlayerTime: AVAudioTime) -> AVAudioTime?](avaudioplayernode/nodetime(forplayertime:).md)
  Converts from player time to node time.
- [func playerTime(forNodeTime: AVAudioTime) -> AVAudioTime?](avaudioplayernode/playertime(fornodetime:).md)
  Converts from node time to player time.
### Controlling Playback
- [func prepare(withFrameCount: AVAudioFrameCount)](avaudioplayernode/prepare(withframecount:).md)
  Prepares the file regions or buffers you schedule for playback.
- [func play()](avaudioplayernode/play.md)
  Starts or resumes playback immediately.
- [func play(at: AVAudioTime?)](avaudioplayernode/play(at:).md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](avaudioplayernode/isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](avaudioplayernode/pause.md)
  Pauses the node’s playback.
- [func stop()](avaudioplayernode/stop.md)
  Clears all of the node’s events you schedule and stops playback.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Playing custom audio with your own player](playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [Using voice processing](using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode)*