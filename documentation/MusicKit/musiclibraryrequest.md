# MusicLibraryRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch items from the user’s music library.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct MusicLibraryRequest<MusicItemType> where MusicItemType : MusicLibraryRequestable
```

## Topics

### Initializers
- [init()](musiclibraryrequest/init.md)
  Creates a request to fetch items from the library.
### Instance Properties
- [var includeOnlyDownloadedContent: Bool](musiclibraryrequest/includeonlydownloadedcontent.md)
  A Boolean value that indicates whether the library response should only include items downloaded on the user’s device.
- [var limit: Int](musiclibraryrequest/limit.md)
  A limit for the number of items to return in the library response.
- [var offset: Int](musiclibraryrequest/offset.md)
  An offset for the request.
### Instance Methods
- [func filter(matching: KeyPath<MusicItemType.LibraryFilter, String?>, contains: String)](musiclibraryrequest/filter(matching:contains:)-4q231.md)
  Filters items by a given optional property that contains a specific string.
- [func filter(matching: KeyPath<MusicItemType.LibraryFilter, String>, contains: String)](musiclibraryrequest/filter(matching:contains:)-8wwn3.md)
  Filters items by a given property that contains a specific string.
- [func filter<RelatedMusicItemType>(matching: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>, contains: RelatedMusicItemType)](musiclibraryrequest/filter(matching:contains:)-9756l.md)
  Filters items by a given relationship that matches a specific value.
- [func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo: Value)](musiclibraryrequest/filter(matching:equalto:)-5jgfj.md)
  Filters items by a given property that matches a specific value.
- [func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, equalTo: Value?)](musiclibraryrequest/filter(matching:equalto:)-8efya.md)
  Filters items by a given optional property that matches a specific value.
- [func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf: [Value?])](musiclibraryrequest/filter(matching:memberof:)-2u2ia.md)
  Filters items by an optional property for an array of possible values.
- [func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, memberOf: [Value])](musiclibraryrequest/filter(matching:memberof:)-3e2ab.md)
  Filters items by a property for an array of possible values.
- [func filter(text: String)](musiclibraryrequest/filter(text:).md)
  Filters items by a specific string.
- [func response() async throws -> MusicLibraryResponse<MusicItemType>](musiclibraryrequest/response.md)
  Fetches items from the user’s music library.
- [func sort<Value>(by: KeyPath<MusicItemType.LibrarySortProperties, Value>, ascending: Bool)](musiclibraryrequest/sort(by:ascending:).md)
  Sorts items by a specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibraryrequest)*