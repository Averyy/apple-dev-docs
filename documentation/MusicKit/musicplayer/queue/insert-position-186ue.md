# insert(_:position:)

**Framework**: MusicKit  
**Kind**: method

Inserts a playable music item into the playback queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func insert<PlayableMusicItemType>(_ playableItem: PlayableMusicItemType, position: MusicPlayer.Queue.EntryInsertionPosition) async throws where PlayableMusicItemType : PlayableMusicItem
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/insert(_:position:)-186ue)*