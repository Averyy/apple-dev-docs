# loops

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the audio source should play repeatedly.

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
var loops: Bool { get set }
```

```objc
@property (nonatomic) BOOL loops;
```

#### Discussion

If this value is [`true`](../../Swift/true.md), audio players using this source automatically begin playing again after playback has finished. If this value is [`false`](../../Swift/false.md) (the default), the audio source plays exactly once.

## See Also

### Setting Default Playback Parameters
- [var volume: Float](./volume.md)
  The default playback volume for the audio source.
- [var rate: Float](./rate.md)
  The default playback rate for the audio source.
- [var reverbBlend: Float](./reverbblend.md)
  The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.
- [var shouldStream: Bool](./shouldstream.md)
  A Boolean value that determines whether the audio source should stream content from its source URL when playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/loops)*