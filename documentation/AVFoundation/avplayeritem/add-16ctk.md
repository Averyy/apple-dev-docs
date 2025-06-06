# add(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds the specified player item output object to the receiver.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@MainActor
func add(_ output: AVPlayerItemOutput)
```

#### Discussion

When you add an [`AVPlayerItemOutput`](avplayeritemoutput.md) object to an item, the samples associated with that output object are processed according to the rules for mixing, composing, or excluding content that the [`AVPlayer`](avplayer.md) object honors for the specific media type. For example, video media is composed according to the instructions provided by the player item’s video composition object and audio media is mixed according to the parameters of its audio mix object.

## Parameters

- `output`: The player item output object to associate with the item.

## See Also

- [var audioMix: AVAudioMix?](avplayeritem/audiomix.md)
  The audio mix parameters to be applied during playback.
- [var videoComposition: AVVideoComposition?](avplayeritem/videocomposition.md)
  The video composition settings to be applied during playback.
- [var outputs: [AVPlayerItemOutput]](avplayeritem/outputs.md)
  An array of outputs associated with the player item.
- [func remove(AVPlayerItemOutput)](avplayeritem/remove(_:)-46b1r.md)
  Removes the specified player item output object from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/add(_:)-16ctk)*