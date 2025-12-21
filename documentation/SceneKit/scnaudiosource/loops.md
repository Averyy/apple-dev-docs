# loops

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the audio source should play repeatedly.

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
var loops: Bool { get set }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/Swift/true), audio players using this source automatically begin playing again after playback has finished. If this value is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), the audio source plays exactly once.

## See Also

- [var volume: Float](scnaudiosource/volume.md)
  The default playback volume for the audio source.
- [var rate: Float](scnaudiosource/rate.md)
  The default playback rate for the audio source.
- [var reverbBlend: Float](scnaudiosource/reverbblend.md)
  The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.
- [var shouldStream: Bool](scnaudiosource/shouldstream.md)
  A Boolean value that determines whether the audio source should stream content from its source URL when playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/loops)*