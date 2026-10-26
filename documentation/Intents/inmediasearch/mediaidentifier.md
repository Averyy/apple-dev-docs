# mediaIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique media identifier to search for.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mediaIdentifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * mediaIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * mediaIdentifier;
```

#### Discussion

This property is only populated when your app is the currently playing app. It’s only present for currently playing reference items.

## See Also

### Retrieving Search Information
- [var genreNames: [String]?](./genrenames.md)
  The media genres to search.
- [var mediaName: String?](./medianame.md)
  The name of the media to search for.
- [var mediaType: INMediaItemType](./mediatype.md)
  The type of media to search for.
- [var moodNames: [String]?](./moodnames.md)
  The moods to search for.
- [var reference: INMediaReference](./reference.md)
  A reference for the media item to search for.
- [enum INMediaReference](../inmediareference.md)
  Constants that describe a reference for a media item.
- [var releaseDate: INDateComponentsRange?](./releasedate.md)
  The release date to search for.
- [var sortOrder: INMediaSortOrder](./sortorder.md)
  The sort order for the found media items.
- [enum INMediaSortOrder](../inmediasortorder.md)
  Constants indicating the sort order for the found media items.
- [var activityNames: [String]?](./activitynames.md)
  The activity names to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediasearch/mediaidentifier)*