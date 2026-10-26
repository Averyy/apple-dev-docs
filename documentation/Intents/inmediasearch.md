# INMediaSearch

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes a media type to search for, such as a station name, song name, or album name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INMediaSearch
```

```objc
@interface INMediaSearch : NSObject
```

## Topics

### Initializing a Media Search Object
- [convenience init(mediaType: INMediaItemType, sortOrder: INMediaSortOrder, mediaName: String?, artistName: String?, albumName: String?, genreNames: [String]?, moodNames: [String]?, releaseDate: INDateComponentsRange?, reference: INMediaReference, mediaIdentifier: String?)](./inmediasearch/init%28mediatype,sortorder,medianame,artistname,albumname,genrenames,moodnames,releasedate,reference,mediaidentifier%29.md)
  Creates a new media search object with the specified parameters.
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
- [enum INMediaSortOrder](./inmediasortorder.md)
  Constants indicating the sort order for the found media items.
- [var activityNames: [String]?](./inmediasearch/activitynames.md)
  The activity names to search for.
### Modifying the Media Name
- [var albumName: String?](./inmediasearch/albumname.md)
  The name of the album to search for.
- [var artistName: String?](./inmediasearch/artistname.md)
  The name of the artist to search for.
### Initializers
- [init?(coder: NSCoder)](./inmediasearch/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [class INMediaItem](./inmediaitem.md)
  An object that describes a piece of media content, such as a song, TV show, artist, or podcast playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediasearch)*