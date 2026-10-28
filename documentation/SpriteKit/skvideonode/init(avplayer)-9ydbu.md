# init(avPlayer:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a video node using an existing [`AVPlayer`](../../AVFoundation/avplayer.md) object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(avPlayer player: AVPlayer)
```

```objc
- (instancetype) initWithAVPlayer:(AVPlayer *) player;
```

## Return Value

An initialized video node.

## Discussion

You can use the [`AVPlayer`](../../AVFoundation/avplayer.md) object to control playback.

Listing 1 shows, in Swift, how you can create a video node using the [`init(avPlayer:)`](./init%28avplayer%29-9ydbu.md) initializer.

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

### Creating a Video Node
- [init(fileNamed: String)](./init%28filenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](./init%28url%29-2im38.md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](./init%28videofilenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
- [init(videoURL: URL)](./init%28videourl%29.md)
  Initializes a video node using a URL that points to a video file.
- [+ videoNodeWithFileNamed:](./videonodewithfilenamed_.md)
  Creates and initializes a new video node using a video file stored in the app bundle.
- [+ videoNodeWithAVPlayer:](./videonodewithavplayer_.md)
  Creates and initializes a video node using an existing video player object.
- [+ videoNodeWithURL:](./videonodewithurl_.md)
  Creates and initializes a video node using a URL that points to a video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(avplayer:)-9ydbu)*