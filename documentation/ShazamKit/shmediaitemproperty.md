# SHMediaItemProperty

**Framework**: ShazamKit  
**Kind**: struct

Constants for the media item property names.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SHMediaItemProperty
```

## Topics

### Creating a property key
- [init(String)](shmediaitemproperty/init(_:).md)
  Creates a property key for the specified property.
- [init(rawValue: String)](shmediaitemproperty/init(rawvalue:).md)
  Creates a property key for the specified property.
### General media item property keys
- [static let title: SHMediaItemProperty](shmediaitemproperty/title.md)
  The key to access the title property of a media item.
- [static let subtitle: SHMediaItemProperty](shmediaitemproperty/subtitle.md)
  The key to access the subtitle property of a media item.
- [static let artist: SHMediaItemProperty](shmediaitemproperty/artist.md)
  The key to access the artist property of a media item.
- [static let artworkURL: SHMediaItemProperty](shmediaitemproperty/artworkurl.md)
  The key to access the artwork URL property of a media item.
- [static let videoURL: SHMediaItemProperty](shmediaitemproperty/videourl.md)
  The key to access the video URL property of a media item.
- [static let genres: SHMediaItemProperty](shmediaitemproperty/genres.md)
  The key to access the genres property of a media item.
- [static let explicitContent: SHMediaItemProperty](shmediaitemproperty/explicitcontent.md)
  The key to access the explicit content property of a media item.
- [static let ISRC: SHMediaItemProperty](shmediaitemproperty/isrc.md)
  The key to access the International Standard Recording Code (ISRC) property of a media item.
- [static let frequencySkewRanges: SHMediaItemProperty](shmediaitemproperty/frequencyskewranges.md)
  The key to access the frequency skew ranges property of a media item.
- [static let creationDate: SHMediaItemProperty](shmediaitemproperty/creationdate.md)
  The date the media item was created.
- [static let timeRanges: SHMediaItemProperty](shmediaitemproperty/timeranges.md)
  The key to access the time ranges property of a media item.
### Apple Music property keys
- [static let appleMusicURL: SHMediaItemProperty](shmediaitemproperty/applemusicurl.md)
  The key to access the Apple Music URL property of a media item.
- [static let appleMusicID: SHMediaItemProperty](shmediaitemproperty/applemusicid.md)
  The key to access the Apple Music ID of a media item.
### Shazam music catalog property keys
- [static let webURL: SHMediaItemProperty](shmediaitemproperty/weburl.md)
  The key to access the web URL property of a media item.
- [static let shazamID: SHMediaItemProperty](shmediaitemproperty/shazamid.md)
  The key to access the Shazam ID property of a media item.
### Matched media item property keys
- [static let matchOffset: SHMediaItemProperty](shmediaitemproperty/matchoffset.md)
  The key to access the match offset property of a matched media item.
- [static let frequencySkew: SHMediaItemProperty](shmediaitemproperty/frequencyskew.md)
  The key to access the frequency skew property of a matched media item.
### Type Properties
- [static let confidence: SHMediaItemProperty](shmediaitemproperty/confidence.md)
  The value ranges from 0.0 to 1.0, where 1.0 indicates the highest level of confidence.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [subscript(SHMediaItemProperty) -> Any](shmediaitem/subscript(_:).md)
  Accesses the property for the specified key for reading.
- [var timeRanges: [Range<TimeInterval>]](shmediaitem/timeranges-8msna.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [var frequencySkewRanges: [Range<Float>]](shmediaitem/frequencyskewranges-1j7d3.md)
  An array of ranges that indicate the frequency skews in the reference signature that this media item describes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitemproperty)*