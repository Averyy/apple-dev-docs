# compilations()

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Creates a media query that matches compilation items and that groups and sorts collections by album name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func compilations() -> MPMediaQuery
```

```objc
+ (MPMediaQuery *) compilationsQuery;
```

#### Return Value

A media query that matches any media item that has the [`MPMediaItemPropertyIsCompilation`](../mpmediaitempropertyiscompilation.md) property; the returned query has a grouping type of [`MPMediaGrouping.album`](../mpmediagrouping/album.md).

#### Discussion

A media item can have more than one media type; for example, an item could be of types “music” and “podcast.” A [`compilations()`](./compilations%28%29.md) query matches all media items that have the [`MPMediaItemPropertyIsCompilation`](../mpmediaitempropertyiscompilation.md) property, irrespective of their media types.

## See Also

### Creating media queries
- [class func albums() -> MPMediaQuery](./albums%28%29.md)
  Creates a media query that matches music items and that groups and sorts collections by album name.
- [class func artists() -> MPMediaQuery](./artists%28%29.md)
  Creates a media query that matches music items and that groups and sorts collections by artist name.
- [class func songs() -> MPMediaQuery](./songs%28%29.md)
  Creates a media query that matches music items and that groups and sorts collections by song name.
- [class func playlists() -> MPMediaQuery](./playlists%28%29.md)
  Creates a media query that matches the entire library and that groups and sorts collections by playlist name.
- [class func podcasts() -> MPMediaQuery](./podcasts%28%29.md)
  Creates a media query that matches podcast items and that groups and sorts collections by podcast name.
- [class func audiobooks() -> MPMediaQuery](./audiobooks%28%29.md)
  Creates a media query that matches audio book items and that groups and sorts collections by audio book name.
- [class func composers() -> MPMediaQuery](./composers%28%29.md)
  Creates a media query that matches all media items and that groups and sorts collections by composer name.
- [class func genres() -> MPMediaQuery](./genres%28%29.md)
  Creates a media query that matches all media items and that groups and sorts collections by genre name.
- [init(filterPredicates: Set<MPMediaPredicate>?)](./init%28filterpredicates%29.md)
  Initializes a media query with a set of media property predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/compilations())*