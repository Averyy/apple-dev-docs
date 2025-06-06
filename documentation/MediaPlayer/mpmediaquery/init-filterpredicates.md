# init(filterPredicates:)

**Framework**: Media Player  
**Kind**: init

Initializes a media query with a set of media property predicates.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(filterPredicates: Set<MPMediaPredicate>?)
```

#### Return Value

An initialized media query.

#### Discussion

[`MPMediaPropertyPredicate`](mpmediapropertypredicate.md) describes how to create media property predicates. The [`General media item property keys`](general-media-item-property-keys.md) and `Podcast Item Property Keys` enumerations in [`MPMediaItem`](mpmediaitem.md) contain the keys you can use to construct predicates.

## Parameters

- `filterPredicates`: The set of media property predicates to use as a filter on the library.

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
- [class func audiobooks() -> MPMediaQuery](mpmediaquery/audiobooks.md)
  Creates a media query that matches audio book items and that groups and sorts collections by audio book name.
- [class func compilations() -> MPMediaQuery](mpmediaquery/compilations.md)
  Creates a media query that matches compilation items and that groups and sorts collections by album name.
- [class func composers() -> MPMediaQuery](mpmediaquery/composers.md)
  Creates a media query that matches all media items and that groups and sorts collections by composer name.
- [class func genres() -> MPMediaQuery](mpmediaquery/genres.md)
  Creates a media query that matches all media items and that groups and sorts collections by genre name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/init(filterpredicates:))*