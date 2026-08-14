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
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [MusicItem](musicitem.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [MusicVideo](musicvideo.md)
- [Song](song.md)
- [Track](track.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/pickablemusicitem)*