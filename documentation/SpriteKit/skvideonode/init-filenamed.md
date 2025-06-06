# init(fileNamed:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a video node using a video file stored in the app bundle.

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
init(fileNamed videoFile: String)
```

#### Return Value

An initialized video node.

## Parameters

- `videoFile`: The name of the video file.

## See Also

- [init(avPlayer: AVPlayer)](skvideonode/init(avplayer:).md)
  Initializes a video node using an existing [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object.
- [init(url: URL)](skvideonode/init(url:).md)
  Initializes a video node using a URL.
- [init?(coder: NSCoder)](skvideonode/init(coder:).md)
  Tells you when to initialize a video node that was created from an archive.
- [init(videoFileNamed: String)](skvideonode/init(videofilenamed:).md)
  Initializes a video node using a video file stored in the app bundle.
- [init(videoURL: URL)](skvideonode/init(videourl:).md)
  Initializes a video node using a URL that points to a video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skvideonode/init(filenamed:))*