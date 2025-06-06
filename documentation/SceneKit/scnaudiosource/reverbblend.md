# reverbBlend

**Framework**: SceneKit  
**Kind**: property

The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var reverbBlend: Float { get set }
```

#### Discussion

This property determines the default reverb blend for when a source begins playing. To vary the reverb blend during playback through an [`SCNAudioPlayer`](scnaudioplayer.md) object, use the player’s [`audioNode`](scnaudioplayer/audionode.md) property to access real-time audio controls.

## See Also

- [var volume: Float](scnaudiosource/volume.md)
  The default playback volume for the audio source.
- [var rate: Float](scnaudiosource/rate.md)
  The default playback rate for the audio source.
- [var loops: Bool](scnaudiosource/loops.md)
  A Boolean value that determines whether the audio source should play repeatedly.
- [var shouldStream: Bool](scnaudiosource/shouldstream.md)
  A Boolean value that determines whether the audio source should stream content from its source URL when playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/reverbblend)*