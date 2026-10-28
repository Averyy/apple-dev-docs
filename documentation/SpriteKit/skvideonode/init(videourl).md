# init(videoURL:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a video node using a URL that points to a video file.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`init(url:)`](./init%28url%29-2im38.md) instead.

## Declaration

```swift
init(videoURL url: URL)
```

```objc
- (instancetype) initWithVideoURL:(NSURL *) url;
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
- [init(url: URL)](./init%28url%29-2im38.md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](./init%28videofilenamed%29.md)
  Initializes a video node using a video file stored in the app bundle.
- [+ videoNodeWithFileNamed:](./videonodewithfilenamed_.md)
  Creates and initializes a new video node using a video file stored in the app bundle.
- [+ videoNodeWithAVPlayer:](./videonodewithavplayer_.md)
  Creates and initializes a video node using an existing video player object.
- [+ videoNodeWithURL:](./videonodewithurl_.md)
  Creates and initializes a video node using a URL that points to a video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(videourl:))*