# AVAudioPlayerNode

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioPlayerNode : AVAudioNode
```

## Overview

This audio node supports scheduling the playback of [`AVAudioPCMBuffer`](./avaudiopcmbuffer.md) instances, or segments of audio files that you open through [`AVAudioFile`](./avaudiofile.md). You can schedule buffers and segments to play at specific points in time or to play immediately following preceding segments.

Generally, you want to configure the node’s output format with the same number of channels as in the files and buffers. Otherwise, the node drops or adds channels as necessary. It’s usually preferable to use an [`AVAudioMixerNode`](./avaudiomixernode.md) for this configuration.

Similarly, when playing file segments, the node makes sample rate conversions, if necessary. It’s preferable to configure the node’s output sample rate to match that of the files, and to use a mixer to perform the rate conversion.

When playing buffers, there’s an implicit assumption that the buffers are at the same sample rate as the node’s output format.

The [`stop()`](./avaudioplayernode/stop%28%29.md) method unschedules all previously scheduled buffers and file segments, and returns the player timeline to sample time `0`.

> **Note**:  The `AVAudioPlayerNode` class isn’t key-value observing compliant, and may indicate that Combine publishers are available. Don’t use them for monitoring changes.

### Player timeline

The usual [`AVAudioNode`](./avaudionode.md) sample times, which [`lastRenderTime`](./avaudionode/lastrendertime.md) observes, have an arbitrary zero point. The `AVAudioPlayerNode` class superimposes a second player timeline on top of this to reflect when the player starts and intervals when it pauses. The methods [`nodeTime(forPlayerTime:)`](./avaudioplayernode/nodetime%28forplayertime%29.md) and [`playerTime(forNodeTime:)`](./avaudioplayernode/playertime%28fornodetime%29.md) convert between the two.

### Scheduling playback time

The [`scheduleBuffer(_:at:options:completionHandler:)`](./avaudioplayernode/schedulebuffer%28_,at,options,completionhandler%29.md), [`scheduleFile(_:at:completionHandler:)`](./avaudioplayernode/schedulefile%28_,at,completionhandler%29.md), and [`scheduleSegment(_:startingFrame:frameCount:at:completionHandler:)`](./avaudioplayernode/schedulesegment%28_,startingframe,framecount,at,completionhandler%29.md) methods take an [`AVAudioTime`](./avaudiotime.md) `when` parameter, and you interpret it as follows:

- If the `when` parameter is `nil`:
- If there are previous commands, the new one plays immediately following the last one.
- Otherwise, if the node is in a playing state, the event plays in the very near future.
- Otherwise, the command plays at sample time `0`.
- If the `when` parameter is a sample time, the parameter interprets it as such.
- If the `when` parameter is a host time, the system ignores it unless the sample time is invalid when the engine is rendering to an audio device.

The scheduling methods fail if:

- A buffer’s channel count doesn’t match that of the node’s output format.
- The system can’t access a file.
- An [`AVAudioTime`](./avaudiotime.md) doesn’t specify a valid sample time or a host time.
- A segment’s start frame or frame count is a negative value.

### Handling buffer or file completion

The buffer of file completion handlers are a means to schedule more data if available on the player node. For more information on the different completion callback types, see [`AVAudioPlayerNodeCompletionCallbackType`](./avaudioplayernodecompletioncallbacktype.md).

> ❗ **Important**:  Don’t stop a player within a completion handler callback because it can deadlock while trying to unschedule already scheduled buffers.

### Rendering offline

When you use a player node with the engine operating in manual rendering mode, you use the buffer or file completion handlers — [`lastRenderTime`](./avaudionode/lastrendertime.md), [`latency`](./avaudionode/latency.md), and [`outputPresentationLatency`](./avaudionode/outputpresentationlatency.md) — to track how much data the player rendered and how much remains to render.

## Topics

### Creating a player node
- [init()](./avaudioplayernode/init%28%29.md)
  Creates an initialized audio player node.
### Scheduling files and segments
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulefile%28_,at,completionhandler%29.md)
  Schedules the playing of an entire audio file.
- [func scheduleFile(AVAudioFile, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulefile%28_,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an entire audio file with a callback option you specify.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulesegment%28_,startingframe,framecount,at,completionhandler%29.md)
  Schedules the playing of an audio file segment.
- [func scheduleSegment(AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulesegment%28_,startingframe,framecount,at,completioncallbacktype,completionhandler%29.md)
  Schedules the playing of an audio file segment with a callback option you specify.
- [enum AVAudioPlayerNodeCompletionCallbackType](./avaudioplayernodecompletioncallbacktype.md)
  Constants that specify when the framework must invoke the completion handler.
- [typealias AVAudioPlayerNodeCompletionHandler](./avaudioplayernodecompletionhandler.md)
  The callback handler for buffer or file completion.
- [typealias AVAudioNodeCompletionHandler](./avaudionodecompletionhandler.md)
  A general callback handler for an audio node.
### Scheduling buffers
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,at,options,completionhandler%29.md)
  Schedules the playing samples from an audio buffer at the time and playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,completionhandler%29.md)
  Schedules the playing samples from an audio buffer.
- [func scheduleBuffer(AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulebuffer%28_,at,options,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the playback options you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: ((AVAudioPlayerNodeCompletionCallbackType) -> Void)?)](./avaudioplayernode/schedulebuffer%28_,completioncallbacktype,completionhandler%29.md)
  Schedules the playing samples from an audio buffer with the callback option you specify.
- [func scheduleBuffer(AVAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-3ewd3.md)
  Schedules playing samples from an audio buffer.
- [func scheduleBuffer(AVReadOnlyAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionCallbackType: AVAudioPlayerNodeCompletionCallbackType, completionHandler: (() -> Void)?)](./avaudioplayernode/schedulebuffer%28_,attime,options,completioncallbacktype,completionhandler%29-81qje.md)
  Schedules playing samples from a read-only audio buffer.
- [struct AVAudioPlayerNodeBufferOptions](./avaudioplayernodebufferoptions.md)
  The buffer options that control the playback scheduling.
### Converting node and player times
- [func nodeTime(forPlayerTime: AVAudioTime) -> AVAudioTime?](./avaudioplayernode/nodetime%28forplayertime%29.md)
  Converts from player time to node time.
- [func playerTime(forNodeTime: AVAudioTime) -> AVAudioTime?](./avaudioplayernode/playertime%28fornodetime%29.md)
  Converts from node time to player time.
### Controlling playback
- [func prepare(withFrameCount: AVAudioFrameCount)](./avaudioplayernode/prepare%28withframecount%29.md)
  Prepares the file regions or buffers you schedule for playback.
- [func playAudio() throws](./avaudioplayernode/playaudio%28%29.md)
- [func playAudio(at: AVAudioTime?) throws](./avaudioplayernode/playaudio%28at%29.md)
- [func play()](./avaudioplayernode/play%28%29.md)
  Starts or resumes playback immediately.
- [func play(at: AVAudioTime?)](./avaudioplayernode/play%28at%29.md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](./avaudioplayernode/isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](./avaudioplayernode/pause%28%29.md)
  Pauses the node’s playback.
- [func stop()](./avaudioplayernode/stop%28%29.md)
  Clears all of the node’s events you schedule and stops playback.

## Relationships

### Inherits From
- [AVAudioNode](./avaudionode.md)
### Conforms To
- [AVAudio3DMixing](./avaudio3dmixing.md)
- [AVAudioMixing](./avaudiomixing.md)
- [AVAudioStereoMixing](./avaudiostereomixing.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scheduled playback
- [Building an audio sequencer to arrange and play clips](./building-an-audio-sequencer-to-arrange-and-play-clips.md)
  Synchronize audio loops with a main tempo by creating a real-time clip launcher.
- [Playing custom audio with your own player](./playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode)*