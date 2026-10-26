# audiobooks()

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Creates a media query that matches audio book items and that groups and sorts collections by audio book name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func audiobooks() -> MPMediaQuery
```

```objc
+ (MPMediaQuery *) audiobooksQuery;
```

#### Return Value

A media query that matches media items of type [`audioBook`](../mpmediatype/audiobook.md) and that uses the default grouping type of [`MPMediaGrouping.title`](../mpmediagrouping/title.md).

#### Discussion

A media item can have more than one media type; for example, an item could be of types “music” and “podcast.” An [`audiobooks()`](./audiobooks%28%29.md) query matches all [`audioBook`](../mpmediatype/audiobook.md) items, whether or not they’re also of other media types.

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
- [class func compilations() -> MPMediaQuery](./compilations%28%29.md)
  Creates a media query that matches compilation items and that groups and sorts collections by album name.
- [class func composers() -> MPMediaQuery](./composers%28%29.md)
  Creates a media query that matches all media items and that groups and sorts collections by composer name.
- [class func genres() -> MPMediaQuery](./genres%28%29.md)
  Creates a media query that matches all media items and that groups and sorts collections by genre name.
- [init(filterPredicates: Set<MPMediaPredicate>?)](./init%28filterpredicates%29.md)
  Initializes a media query with a set of media property predicates.
- [init](../mpmediaquery-init.md)
  Initializes a generic media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/audiobooks())*