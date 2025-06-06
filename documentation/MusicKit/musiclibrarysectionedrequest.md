# MusicLibrarySectionedRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch items grouped by sections from the user’s music library.

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
struct MusicLibrarySectionedRequest<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable
```

## Topics

### Initializers
- [init()](musiclibrarysectionedrequest/init.md)
  Creates a request to fetch items grouped by sections from the library.
### Instance Properties
- [var includeOnlyDownloadedContent: Bool](musiclibrarysectionedrequest/includeonlydownloadedcontent.md)
  A Boolean value that indicates whether the library response should only include items downloaded on the user’s device.
- [var limit: Int](musiclibrarysectionedrequest/limit.md)
  A limit for the number of items to return in the library response.
- [var offset: Int](musiclibrarysectionedrequest/offset.md)
  An offset for the request.
### Instance Methods
- [func filterItems<RelatedMusicItemType>(matching: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>, contains: RelatedMusicItemType)](musiclibrarysectionedrequest/filteritems(matching:contains:)-3s88f.md)
  Filters items by a given relationship that matches a specific value.
- [func filterItems(matching: KeyPath<MusicItemType.LibraryFilter, String>, contains: String)](musiclibrarysectionedrequest/filteritems(matching:contains:)-8rbsc.md)
  Filters items by a given property that contains a specific string.
- [func filterItems(matching: KeyPath<MusicItemType.LibraryFilter, String?>, contains: String)](musiclibrarysectionedrequest/filteritems(matching:contains:)-9hpfh.md)
  Filters items by a given optional property that contains a specific string.
- [func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo: Value)](musiclibrarysectionedrequest/filteritems(matching:equalto:)-3zn4r.md)
  Filters items by a given property that matches a specific value.
- [func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, equalTo: Value?)](musiclibrarysectionedrequest/filteritems(matching:equalto:)-5ybaa.md)
  Filters items by a given optional property that matches a specific value.
- [func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, memberOf: [Value])](musiclibrarysectionedrequest/filteritems(matching:memberof:)-49h2x.md)
  Filters items by a property for an array of possible values.
- [func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf: [Value?])](musiclibrarysectionedrequest/filteritems(matching:memberof:)-zmb0.md)
  Filters items by an optional property for an array of possible values.
- [func filterItems(text: String)](musiclibrarysectionedrequest/filteritems(text:).md)
  Filters items by a specific string.
- [func filterSections(matching: KeyPath<SectionType.LibraryFilter, String?>, contains: String)](musiclibrarysectionedrequest/filtersections(matching:contains:)-3jf7b.md)
  Filters sections by a given optional property that contains a specific string.
- [func filterSections(matching: KeyPath<SectionType.LibraryFilter, String>, contains: String)](musiclibrarysectionedrequest/filtersections(matching:contains:)-5ptoy.md)
  Filters sections by a given property that contains a specific string.
- [func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value?>, equalTo: Value?)](musiclibrarysectionedrequest/filtersections(matching:equalto:)-5nop7.md)
  Filters sections by a given optional property that matches a specific value.
- [func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value>, equalTo: Value)](musiclibrarysectionedrequest/filtersections(matching:equalto:)-7v8tr.md)
  Filters sections by a given property that matches a specific value.
- [func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value>, memberOf: [Value])](musiclibrarysectionedrequest/filtersections(matching:memberof:)-4l0z8.md)
  Filters sections by a property for an array of possible values.
- [func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value?>, memberOf: [Value?])](musiclibrarysectionedrequest/filtersections(matching:memberof:)-746mb.md)
  Filters sections by an optional property for an array of possible values.
- [func filterSections(text: String)](musiclibrarysectionedrequest/filtersections(text:).md)
  Filters sections by a specific string.
- [func response() async throws -> MusicLibrarySectionedResponse<SectionType, MusicItemType>](musiclibrarysectionedrequest/response.md)
  Fetches items grouped by sections from the user’s music library.
- [func sortItems<Value>(by: KeyPath<MusicItemType.LibrarySortProperties, Value>, ascending: Bool)](musiclibrarysectionedrequest/sortitems(by:ascending:).md)
  Sorts items by a specified property.
- [func sortSections<Value>(by: KeyPath<SectionType.LibrarySortProperties, Value>, ascending: Bool)](musiclibrarysectionedrequest/sortsections(by:ascending:).md)
  Sorts sections by a specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest)*