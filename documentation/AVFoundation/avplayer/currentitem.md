# currentItem

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The item for which the player is currently controlling playback.

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
nonisolated
var currentItem: AVPlayerItem? { get }
```

```objc
@property (readonly, nullable) AVPlayerItem * currentItem;
```

## Mentions

- [Observing playback state in SwiftUI](../observing-playback-state-in-swiftui.md)

## See Also

### Managing the player item
- [func replaceCurrentItem(with: AVPlayerItem?)](./replacecurrentitem%28with%29.md)
  Replaces the current item with a new item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/currentitem)*