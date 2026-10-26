# INMediaReference

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe a reference for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INMediaReference
```

```c
enum INMediaReference : NSInteger;
```

## Topics

### Getting the Reference Status
- [INMediaReference.unknown](./inmediareference/unknown.md)
  Indicates that the media item is unknown.
- [INMediaReference.currentlyPlaying](./inmediareference/currentlyplaying.md)
  Indicates that the user is referring to the media item which is currently playing.
- [INMediaReference.my](./inmediareference/my.md)
  Indicates that the specified content belongs to the user.
### Initializers
- [init?(rawValue: Int)](./inmediareference/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Retrieving Search Information
- [var genreNames: [String]?](./inmediasearch/genrenames.md)
  The media genres to search.
- [var mediaIdentifier: String?](./inmediasearch/mediaidentifier.md)
  The unique media identifier to search for.
- [var mediaName: String?](./inmediasearch/medianame.md)
  The name of the media to search for.
- [var mediaType: INMediaItemType](./inmediasearch/mediatype.md)
  The type of media to search for.
- [var moodNames: [String]?](./inmediasearch/moodnames.md)
  The moods to search for.
- [var reference: INMediaReference](./inmediasearch/reference.md)
  A reference for the media item to search for.
- [var releaseDate: INDateComponentsRange?](./inmediasearch/releasedate.md)
  The release date to search for.
- [var sortOrder: INMediaSortOrder](./inmediasearch/sortorder.md)
  The sort order for the found media items.
- [enum INMediaSortOrder](./inmediasortorder.md)
  Constants indicating the sort order for the found media items.
- [var activityNames: [String]?](./inmediasearch/activitynames.md)
  The activity names to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediareference)*