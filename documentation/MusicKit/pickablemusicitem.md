# PickableMusicItem

**Framework**: MusicKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for the MusicKit item type that can be selected in the music picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol PickableMusicItem : MusicItem, Decodable, Encodable, Hashable
```

## Relationships

### Inherits From
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MusicItem](./musicitem.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [MusicVideo](./musicvideo.md)
- [Song](./song.md)
- [Track](./track.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/pickablemusicitem)*