# MPMediaGrouping

**Framework**: Media Player  
**Kind**: enum

Keys used to configure a media query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum MPMediaGrouping
```

#### Overview

The following code snippet shows how to apply a grouping key:

After running these code lines, the `collections` array contains all the matched media items grouped and sorted according to album name.

To obtain a sorted list of songs, configure a media query with the `MPMediaGroupingTitle` key, or take advantage of the title key being the default for a media query. In either case, each obtained media item is, in effect, its own collection.

Collections sort according to the same rules used by iTunes on the desktop. This includes respecting the primary system language chosen by the user. The system ignores leading articles during sorting, including “A,” “An,” and “The” when using English, or “L’,” “La,” and “Le” when using French. If you need precise control over sorting, implement it in your application.

## Topics

### Media query keys
- [MPMediaGrouping.title](mpmediagrouping/title.md)
  Groups and sorts media item collections by title. For songs, for example, the title is the song name. This is the default grouping key.
- [MPMediaGrouping.album](mpmediagrouping/album.md)
  Groups and sorts media item collections by album, and sorts songs within an album by track order.
- [MPMediaGrouping.artist](mpmediagrouping/artist.md)
  Groups and sorts media item collections by performing artist.
- [MPMediaGrouping.albumArtist](mpmediagrouping/albumartist.md)
  Groups and sorts media item collections by album artist (the primary performing artist for an album as a whole).
- [MPMediaGrouping.composer](mpmediagrouping/composer.md)
  Groups and sorts media item collections by composer.
- [MPMediaGrouping.genre](mpmediagrouping/genre.md)
  Groups and sorts media item collections by musical or film genre.
- [MPMediaGrouping.playlist](mpmediagrouping/playlist.md)
  Groups and sorts media item collections by playlist.
- [MPMediaGrouping.podcastTitle](mpmediagrouping/podcasttitle.md)
  Groups and sorts media item collections by podcast title.
### Initializers
- [init?(rawValue: Int)](mpmediagrouping/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var filterPredicates: Set<MPMediaPredicate>?](mpmediaquery/filterpredicates.md)
  The media property predicates of the media query.
- [func addFilterPredicate(MPMediaPredicate)](mpmediaquery/addfilterpredicate(_:).md)
  Adds a media property predicate to a query.
- [func removeFilterPredicate(MPMediaPredicate)](mpmediaquery/removefilterpredicate(_:).md)
  Removes a filter predicate from a query.
- [var groupingType: MPMediaGrouping](mpmediaquery/groupingtype.md)
  The grouping for collections retrieved with the media query.
- [var itemSections: [MPMediaQuerySection]?](mpmediaquery/itemsections.md)
  An array representing the section grouping of the query’s specified media items.
- [var collectionSections: [MPMediaQuerySection]?](mpmediaquery/collectionsections.md)
  An array representing the section grouping of the query’s specified media item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping)*