# init(coder:)

**Framework**: SpriteKit  
**Kind**: init

Tells you when to initialize a video node that was created from an archive.

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
@MainActor
init?(coder aDecoder: NSCoder)
```

#### Discussion

Do not call this initializer yourself; it is called by the system when you should intialize a video node that was created from an archive.

## See Also

- [init(avPlayer: AVPlayer)](skvideonode/init(avplayer:).md)
  Initializes a video node using an existing [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object.
- [init(fileNamed: String)](skvideonode/init(filenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](skvideonode/init(url:).md)
  Initializes a video node using a URL.
- [init(videoFileNamed: String)](skvideonode/init(videofilenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(videoURL: URL)](skvideonode/init(videourl:).md)
  Initializes a video node using a URL that points to a video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(coder:))*