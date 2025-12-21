# init(videoURL:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a video node using a URL that points to a video file.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(videoURL url: URL)
```

#### Return Value

An initialized video node.

## Parameters

- `url`: The URL for the video to play.

## See Also

- [init(avPlayer: AVPlayer)](skvideonode/init(avplayer:).md)
  Initializes a video node using an existing [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object.
- [init(fileNamed: String)](skvideonode/init(filenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(url: URL)](skvideonode/init(url:).md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](skvideonode/init(coder:).md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](skvideonode/init(videofilenamed:).md)
  Initializes a video node using a video file stored in the app bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(videourl:))*