# ContentAttributes

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Metadata for some media content.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ContentAttributes
```

## Topics

### Providing Artwork
- [object ContentAttributes.Artwork](contentattributes/artwork-data.dictionary.md)
  Imagery for media content, such as an album cover.

## Properties

- `albumName` (string): The album that contains this media content.
- `artistName` (string): The performer of this media content.
- `artwork` (ContentAttributes.Artwork): The album cover or other imagery.
- `composerName` (string): The composer of this media content.
- `durationInMillis` (uint64): The length of the media content in milliseconds.
- `genreNames` ([string]): Genres that apply to this media content.
- `name` (string): The name of the media content.
- `trackNumber` (uint32): The media content’s track number within the album.
- `contentKeyAssetIdentifier` (string)

## See Also

- [object Content](content.md)
  A description of a piece of playback content, such as a song, podcast, or advertisement.
- [type ContentIdentifier](contentidentifier.md)
  An identifier for a song, podcast, ad, or other media content. The identifier must be stable and unique within a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentattributes)*