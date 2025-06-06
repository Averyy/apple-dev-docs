# init(for:startingAt:)

**Framework**: MusicKit  
**Kind**: init

Creates a playback queue with playable music items.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
required init<S, PlayableMusicItemType>(for playableItems: S, startingAt startPlayableItem: S.Element? = nil) where S : Sequence, PlayableMusicItemType : PlayableMusicItem, PlayableMusicItemType == S.Element
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/init(for:startingat:))*