# shouldStream

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the audio source should stream content from its source URL when playing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shouldStream: Bool { get set }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/Swift/true), audio players using this source do not preload audio buffer data, instead reading directly from the source file while playing audio. If this value is [`false`](https://developer.apple.com/documentation/Swift/false), SceneKit loads audio buffer data upon playing audio from the source.

## See Also

- [var volume: Float](scnaudiosource/volume.md)
  The default playback volume for the audio source.
- [var rate: Float](scnaudiosource/rate.md)
  The default playback rate for the audio source.
- [var reverbBlend: Float](scnaudiosource/reverbblend.md)
  The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.
- [var loops: Bool](scnaudiosource/loops.md)
  A Boolean value that determines whether the audio source should play repeatedly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/shouldstream)*