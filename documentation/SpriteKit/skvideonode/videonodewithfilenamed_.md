# videoNodeWithFileNamed:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates and initializes a new video node using a video file stored in the app bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (SKVideoNode *) videoNodeWithFileNamed:(NSString *) videoFile;
```

## Return Value

A new video node.

## Parameters

- `videoFile`: The name of the video file.

## See Also

### Creating a Video Node
- [+ videoNodeWithAVPlayer:](./videonodewithavplayer_.md)
  Creates and initializes a video node using an existing video player object.
- [+ videoNodeWithURL:](./videonodewithurl_.md)
  Creates and initializes a video node using a URL that points to a video file.
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
- [init(videoURL: URL)](./init%28videourl%29.md)
  Initializes a video node using a URL that points to a video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/videonodewithfilenamed:)*