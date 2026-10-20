# SpotlightSearchTool.ContentDomain.Audio

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

Attribute mapping for the audio domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Audio
```

## Topics

### Configuring the domain
- [init(artist: [SearchableItemAttribute]?, album: [SearchableItemAttribute]?, transcription: [SearchableItemAttribute]?, date: [SearchableItemAttribute]?)](./audio-swift.struct/init%28artist,album,transcription,date%29.md)
### Getting the domain attributes
- [var album: [SearchableItemAttribute]?](./audio-swift.struct/album.md)
  Attributes queried for the album. Default: [`album`](../../searchableitemattribute/album.md)
- [var artist: [SearchableItemAttribute]?](./audio-swift.struct/artist.md)
  Attributes queried for the artist. Default: [`artist`](../../searchableitemattribute/artist.md)
- [var date: [SearchableItemAttribute]?](./audio-swift.struct/date.md)
  Attributes queried for the recording date. Default: [`contentCreationDate`](../../searchableitemattribute/contentcreationdate.md)
- [var transcription: [SearchableItemAttribute]?](./audio-swift.struct/transcription.md)
  Attributes queried for transcribed text.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the audio domain
- [static var audio: SpotlightSearchTool.ContentDomain](./audio-swift.type.property.md)
  Music, podcasts, voice memos, and other audio content.
- [static func audio(SpotlightSearchTool.ContentDomain.Audio) -> SpotlightSearchTool.ContentDomain](./audio%28_%29.md)
  Music, podcasts, voice memos, and other audio content with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/audio-swift.struct)*