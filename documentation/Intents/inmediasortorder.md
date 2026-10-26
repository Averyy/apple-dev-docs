# INMediaSortOrder

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the sort order for the found media items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INMediaSortOrder
```

```c
enum INMediaSortOrder : NSInteger;
```

## Topics

### Constants
- [INMediaSortOrder.unknown](./inmediasortorder/unknown.md)
  The sort order is unknown.
- [INMediaSortOrder.newest](./inmediasortorder/newest.md)
  The app sorts the media items from newest to oldest.
- [INMediaSortOrder.oldest](./inmediasortorder/oldest.md)
  The app sorts the media items from oldest to newest.
- [INMediaSortOrder.best](./inmediasortorder/best.md)
  The app sorts the media items from best to worst.
- [INMediaSortOrder.worst](./inmediasortorder/worst.md)
  The app sorts the media items from worst to best.
- [INMediaSortOrder.popular](./inmediasortorder/popular.md)
  The app sorts the media items from the most to least popular.
- [INMediaSortOrder.unpopular](./inmediasortorder/unpopular.md)
  The app sorts the media items from the least to most popular.
- [INMediaSortOrder.trending](./inmediasortorder/trending.md)
  The app sorts the media items with those trending the most first.
- [INMediaSortOrder.recommended](./inmediasortorder/recommended.md)
  The app sorts the media items with those it recommends first.
### Initializers
- [init?(rawValue: Int)](./inmediasortorder/init%28rawvalue%29.md)

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
- [enum INMediaReference](./inmediareference.md)
  Constants that describe a reference for a media item.
- [var releaseDate: INDateComponentsRange?](./inmediasearch/releasedate.md)
  The release date to search for.
- [var sortOrder: INMediaSortOrder](./inmediasearch/sortorder.md)
  The sort order for the found media items.
- [var activityNames: [String]?](./inmediasearch/activitynames.md)
  The activity names to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediasortorder)*