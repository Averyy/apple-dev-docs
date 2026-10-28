# shouldStream

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the audio source should stream content from its source URL when playing.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var shouldStream: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldStream;
```

## Discussion

If this value is [`true`](../../Swift/true.md), audio players using this source do not preload audio buffer data, instead reading directly from the source file while playing audio. If this value is [`false`](../../Swift/false.md), SceneKit loads audio buffer data upon playing audio from the source.

## See Also

### Setting Default Playback Parameters
- [var volume: Float](./volume.md)
  The default playback volume for the audio source.
- [var rate: Float](./rate.md)
  The default playback rate for the audio source.
- [var reverbBlend: Float](./reverbblend.md)
  The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether the audio source should play repeatedly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/shouldstream)*