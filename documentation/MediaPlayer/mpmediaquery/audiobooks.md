# audiobooks()

**Framework**: Media Player  
**Kind**: method

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

#### Return Value

A media query that matches media items of type [`audioBook`](mpmediatype/audiobook.md) and that uses the default grouping type of [`MPMediaGrouping.title`](mpmediagrouping/title.md).

#### Discussion

A media item can have more than one media type; for example, an item could be of types “music” and “podcast.” An [`audiobooks()`](mpmediaquery/audiobooks().md) query matches all [`audioBook`](mpmediatype/audiobook.md) items, whether or not they’re also of other media types.

## See Also

- [class func albums() -> MPMediaQuery](mpmediaquery/albums.md)
  Creates a media query that matches music items and that groups and sorts collections by album name.
- [class func artists() -> MPMediaQuery](mpmediaquery/artists.md)
  Creates a media query that matches music items and that groups and sorts collections by artist name.
- [class func songs() -> MPMediaQuery](mpmediaquery/songs.md)
  Creates a media query that matches music items and that groups and sorts collections by song name.
- [class func playlists() -> MPMediaQuery](mpmediaquery/playlists.md)
  Creates a media query that matches the entire library and that groups and sorts collections by playlist name.
- [class func podcasts() -> MPMediaQuery](mpmediaquery/podcasts.md)
  Creates a media query that matches podcast items and that groups and sorts collections by podcast name.
- [class func compilations() -> MPMediaQuery](mpmediaquery/compilations.md)
  Creates a media query that matches compilation items and that groups and sorts collections by album name.
- [class func composers() -> MPMediaQuery](mpmediaquery/composers.md)
  Creates a media query that matches all media items and that groups and sorts collections by composer name.
- [class func genres() -> MPMediaQuery](mpmediaquery/genres.md)
  Creates a media query that matches all media items and that groups and sorts collections by genre name.
- [init(filterPredicates: Set<MPMediaPredicate>?)](mpmediaquery/init(filterpredicates:).md)
  Initializes a media query with a set of media property predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/audiobooks())*