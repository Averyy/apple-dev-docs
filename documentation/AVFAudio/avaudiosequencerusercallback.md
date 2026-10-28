# AVAudioSequencerUserCallback

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A callback the sequencer calls asynchronously during playback when it encounters a user event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias AVAudioSequencerUserCallback = (AVMusicTrack, Data, AVMusicTimeStamp) -> Void
```

```c
typedef void (^)(AVMusicTrack *, NSData *, double) AVAudioSequencerUserCallback;
```

## Discussion

The sequencer delivers this callback asynchronously to the rendering thread on an internal queue. The `userData` this returns is unique to each [`AVMusicUserEvent`](./avmusicuserevent.md) instance.

## Parameters

- `track`: The track that contains the user event.
- `userData`: The data used to initialize the user event.
- `timeStamp`: The beat location of the event.

## See Also

### Setting the user callback
- [func setUserCallback(AVAudioSequencerUserCallback?)](./avaudiosequencer/setusercallback%28_%29.md)
  Adds a callback that the sequencer calls each time it encounters a user event during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencerusercallback)*