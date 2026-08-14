# SpotlightSearchTool.ContentDomain.Audio

**Framework**: Core Spotlight  
**Kind**: struct

Attribute mapping for the audio domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Audio
```

## Topics

### Configuring the domain
- [init(artist: [SearchableItemAttribute]?, album: [SearchableItemAttribute]?, transcription: [SearchableItemAttribute]?, date: [SearchableItemAttribute]?)](spotlightsearchtool/contentdomain/audio-swift.struct/init(artist:album:transcription:date:).md)
### Getting the domain attributes
- [var album: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/audio-swift.struct/album.md)
  Attributes queried for the album. Default: [`album`](searchableitemattribute/album.md)
- [var artist: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/audio-swift.struct/artist.md)
  Attributes queried for the artist. Default: [`artist`](searchableitemattribute/artist.md)
- [var date: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/audio-swift.struct/date.md)
  Attributes queried for the recording date. Default: [`contentCreationDate`](searchableitemattribute/contentcreationdate.md)
- [var transcription: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/audio-swift.struct/transcription.md)
  Attributes queried for transcribed text.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var audio: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/audio-swift.type.property.md)
  Music, podcasts, voice memos, and other audio content.
- [static func audio(SpotlightSearchTool.ContentDomain.Audio) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/audio(_:).md)
  Music, podcasts, voice memos, and other audio content with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/audio-swift.struct)*