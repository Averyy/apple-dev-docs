# init(avPlayer:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a video node using an existing [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(avPlayer player: AVPlayer)
```

#### Return Value

An initialized video node.

#### Discussion

You can use the [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object to control playback.

Listing 1 shows, in Swift, how you can create a video node using the [`init(avPlayer:)`](skvideonode/init(avplayer:).md) initializer.

Listing 1. Creating a video node with an AV Player

```swift
var videoNode: SKVideoNode? = {
    guard let urlString = Bundle.main.path(forResource: "sample", ofType: "mov") else {
        return nil
    }
    
    let url = URL(fileURLWithPath: urlString)
    let item = AVPlayerItem(url: url)
    let player = AVPlayer(playerItem: item)
    
    return SKVideoNode(avPlayer: player)
}()
```

## Parameters

- `player`: A player object.

## See Also

- [init(fileNamed: String)](skvideonode/init(filenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](skvideonode/init(url:).md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](skvideonode/init(coder:).md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](skvideonode/init(videofilenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(videoURL: URL)](skvideonode/init(videourl:).md)
  Initializes a video node using a URL that points to a video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(avplayer:))*