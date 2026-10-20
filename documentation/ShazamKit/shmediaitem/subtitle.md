# subtitle

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

A subtitle for the media item.

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
var subtitle: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * subtitle;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * subtitle;
```

## See Also

### Reading general media item properties
- [var title: String?](./title.md)
  A title for the media item.
- [var artist: String?](./artist.md)
  The name of the artist for the media item, such as the performer of a song.
- [var artworkURL: URL?](./artworkurl.md)
  The URL for artwork for the media item, such as an album cover.
- [var videoURL: URL?](./videourl.md)
  The URL for a video for the media item, such as a music video.
- [var genres: [String]](./genres.md)
  An array of genre names for the media item.
- [var explicitContent: Bool](./explicitcontent.md)
  A Boolean value that indicates whether the media item contains explicit content.
- [var creationDate: Date?](./creationdate.md)
  The date the media item was created.
- [var isrc: String?](./isrc.md)
  The International Standard Recording Code (ISRC) for the media item.
- [var id: UUID](./id.md)
  A unique identifier for this media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/subtitle)*