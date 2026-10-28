# initWithMediaType:sortOrder:mediaName:artistName:albumName:genreNames:moodNames:releaseDate:reference:mediaIdentifier:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Creates a new media search object with the specified parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (instancetype) initWithMediaType:(INMediaItemType) mediaType sortOrder:(INMediaSortOrder) sortOrder mediaName:(NSString *) mediaName artistName:(NSString *) artistName albumName:(NSString *) albumName genreNames:(NSArray<NSString *> *) genreNames moodNames:(NSArray<NSString *> *) moodNames releaseDate:(INDateComponentsRange *) releaseDate reference:(INMediaReference) reference mediaIdentifier:(NSString *) mediaIdentifier;
```

## Return Value

An initialized search object or `nil` if the object could not be created.

## Parameters

- `mediaType`: The type of media to search for.
- `sortOrder`: The sort order for the media found by the search.
- `mediaName`: The name of the media to search for.
- `artistName`: The name of the artist to search for.
- `albumName`: The name of the album to search for.
- `genreNames`: The different genres to search.
- `moodNames`: The moods to search for. For example, “Play some happy music in ”.
- `releaseDate`: The release date of the media item to search for.
- `reference`: A reference for the media item to search for.
- `mediaIdentifier`: The unique identifier for the media item to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediasearch/initwithmediatype:sortorder:medianame:artistname:albumname:genrenames:moodnames:releasedate:reference:mediaidentifier:)*