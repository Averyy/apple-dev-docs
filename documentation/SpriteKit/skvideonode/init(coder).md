# init(coder:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Tells you when to initialize a video node that was created from an archive.

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
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Discussion

Do not call this initializer yourself; it is called by the system when you should intialize a video node that was created from an archive.

## See Also

### Creating a Video Node
- [init(avPlayer: AVPlayer)](./init%28avplayer%29-9ydbu.md)
  Initializes a video node using an existing [`AVPlayer`](../../AVFoundation/avplayer.md) object.
- [init(fileNamed: String)](./init%28filenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](./init%28url%29-2im38.md)
  Initializes a video node using a URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(coder:))*