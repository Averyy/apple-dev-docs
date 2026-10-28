# play(at:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Starts or resumes playback at a time you specify.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

## Declaration

```swift
func play(at when: AVAudioTime?)
```

```objc
- (void) playAtTime:(AVAudioTime *) when;
```

## Discussion

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

- `when`: The node time to start or resume playback. Passing `nil` starts playback immediately.

## See Also

### Controlling playback
- [func prepare(withFrameCount: AVAudioFrameCount)](./prepare%28withframecount%29.md)
  Prepares the file regions or buffers you schedule for playback.
- [func playAudio() throws](./playaudio%28%29.md)
- [func playAudio(at: AVAudioTime?) throws](./playaudio%28at%29.md)
- [func play()](./play%28%29.md)
  Starts or resumes playback immediately.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](./pause%28%29.md)
  Pauses the node’s playback.
- [func stop()](./stop%28%29.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/play(at:))*