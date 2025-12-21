# controller

**Framework**: RealityKit  
**Kind**: property

An object that configures framework-specific video options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var controller: VideoPlaybackController { get }
```

#### Discussion

Use this property to configure AR-specific properties of the texture’s video, such as whether the material should use spatial audio.

The following example demonstrates enabling spatial audio for a video material:

```swift
material.controller.audioInputMode = .spatial
```

## See Also

- [var avPlayer: AVPlayer?](videomaterial/avplayer.md)
  The material’s video playback controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videomaterial/controller)*