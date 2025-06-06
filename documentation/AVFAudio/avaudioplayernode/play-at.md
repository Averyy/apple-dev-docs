# play(at:)

**Framework**: AVFAudio  
**Kind**: method

Starts or resumes playback at a time you specify.

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
func play(at when: AVAudioTime?)
```

#### Discussion

This node is initially in a paused state. The framework enqueues your requests to play buffers or file segments, and any necessary decoding begins immediately. Playback doesn’t begin until the player starts playing through this method.

The following example code shows how to start a player `0.5` seconds in the future:

```objc
// Start the engine and player.
NSError *nsErr = nil;
[_engine startAndReturnError:&nsErr];
if (!nsErr) {
    const float kStartDelayTime = 0.5; // sec
    AVAudioFormat *outputFormat = [_player outputFormatForBus:0];
    AVAudioFramePosition startSampleTime = _player.lastRenderTime.sampleTime + kStartDelayTime * outputFormat.sampleRate;
    AVAudioTime *startTime = [AVAudioTime timeWithSampleTime:startSampleTime atRate:outputFormat.sampleRate];
    [_player playAtTime:startTime];
}
```

## Parameters

- `when`: The node time to start or resume playback. Passing   starts playback immediately.

## See Also

- [func prepare(withFrameCount: AVAudioFrameCount)](avaudioplayernode/prepare(withframecount:).md)
  Prepares the file regions or buffers you schedule for playback.
- [func play()](avaudioplayernode/play.md)
  Starts or resumes playback immediately.
- [var isPlaying: Bool](avaudioplayernode/isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](avaudioplayernode/pause.md)
  Pauses the node’s playback.
- [func stop()](avaudioplayernode/stop.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/play(at:))*