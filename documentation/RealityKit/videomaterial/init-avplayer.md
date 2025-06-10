# init(avPlayer:)

**Framework**: RealityKit  
**Kind**: init

Creates a new video material.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(avPlayer: AVPlayer)
```

#### Discussion

To create a video material, first create an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) instance initialized with a URL that points to the movie file you want the video material to play, then pass that to this initializer. The following code demonstrates this process.

```swift
// Create a URL that points to the movie file.
if let url = Bundle.main.url(forResource: "MyMovie", withExtension: "mp4") {

    // Create an AVPlayer instance to control playback of that movie.
    let player = AVPlayer(url: url)

    // Instantiate and configure the video material.
    let material = VideoMaterial(avPlayer: player)

    // Configure audio playback mode. This is optional for movie
    // files that contain sound.
    material.controller.audioInputMode = .spatial

    // Create a new model entity using the video material.
    let modelEntity = ModelEntity(mesh: cube, materials: [material])

    // Start playing the video.
    player.play()
}
```

## Parameters

- `avPlayer`: An     instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videomaterial/init(avplayer:))*