# nowPlayingInfo

**Framework**: AVFoundation  
**Kind**: property

The current now playing information for the player item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var nowPlayingInfo: [String : Any]? { get set }
```

#### Discussion

Setting this value to `nil` clears the player item’s now playing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/nowplayinginfo)*