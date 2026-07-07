# PickableMusicItem

**Framework**: MusicKit  
**Kind**: protocol

A protocol for the MusicKit item type that can be selected in the music picker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol PickableMusicItem : MusicItem, Decodable, Encodable, Hashable
```

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MusicItem](musicitem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [MusicVideo](musicvideo.md)
- [Song](song.md)
- [Track](track.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/pickablemusicitem)*