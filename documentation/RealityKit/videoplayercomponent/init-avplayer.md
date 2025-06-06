# init(avPlayer:)

**Framework**: RealityKit  
**Kind**: init

Creates a video player component from an AV player object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(avPlayer: AVPlayer)
```

#### Discussion

> **Note**: You can’t use the same `AVPlayer` object with more than one `VideoPlayerComponent`.

You can’t use the same `AVPlayer` object with more than one `VideoPlayerComponent`.

Here’s an example of setting up a video player component:

```swift
// Create an entity for display.
let videoEntity = Entity()

// Create an AV player with a URL.
let player = AVPlayer(url: "PLACEMENT_URL")

// Create a video player component with the AV player.
let videoPlayerComponent = VideoPlayerComponent(avPlayer: player)

// Attach the video player component to the entity.
videoEntity.components.set(videoPlayerComponent)
```

## Parameters

- `avPlayer`: An     instance.

## See Also

- [init(videoRenderer: AVSampleBufferVideoRenderer)](videoplayercomponent/init(videorenderer:).md)
  Creates a video player component from a sample buffer video renderer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/init(avplayer:))*