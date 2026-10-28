# init(url:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a video node using a URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

## Return Value

An initialized video node.

## Parameters

- `url`: The URL for the video to play.

## See Also

### Creating a Video Node
- [init(avPlayer: AVPlayer)](./init%28avplayer%29-9ydbu.md)
  Initializes a video node using an existing [`AVPlayer`](../../AVFoundation/avplayer.md) object.
- [init(fileNamed: String)](./init%28filenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(url:)-2im38)*