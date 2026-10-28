# reverbBlend

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The default blend of blend of unmodified and reverb-processed (also called dry and wet) audio for playback of the audio source.

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
var reverbBlend: Float { get set }
```

```objc
@property (nonatomic) float reverbBlend;
```

## Discussion

This property determines the default reverb blend for when a source begins playing. To vary the reverb blend during playback through an [`SCNAudioPlayer`](../scnaudioplayer.md) object, use the player’s [`audioNode`](../scnaudioplayer/audionode.md) property to access real-time audio controls.

## See Also

### Setting Default Playback Parameters
- [var volume: Float](./volume.md)
  The default playback volume for the audio source.
- [var rate: Float](./rate.md)
  The default playback rate for the audio source.
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether the audio source should play repeatedly.
- [var shouldStream: Bool](./shouldstream.md)
  A Boolean value that determines whether the audio source should stream content from its source URL when playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/reverbblend)*