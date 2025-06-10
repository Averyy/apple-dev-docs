# canBeginTrimming

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the current media supports trimming.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canBeginTrimming: Bool { get }
```

## Mentions

- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md)

#### Discussion

Not all media supports trimming. For example, this property returns `false` for HTTP Live Streaming media or protected content.

Observe this property to determine when to change the enabled state of your app UI that initiates trimming.

## See Also

- [func beginTrimming(completionHandler: ((Bool) -> Void)?)](avplayerviewcontroller/begintrimming(completionhandler:).md)
  Presents the system trimming interface controls inside the player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/canbegintrimming)*