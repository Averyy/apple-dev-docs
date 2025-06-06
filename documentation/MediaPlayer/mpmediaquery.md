# MPMediaQuery

**Framework**: Media Player  
**Kind**: class

A query that specifies a set of media items from the device’s media library using a filter and a grouping type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaQuery
```

## Mentions

- [Playing audio using the built-in music player](playing-audio-using-the-built-in-music-player.md)

#### Overview

Filter and grouping types are both optional; an unqualified query matches the entire library.

A query has at most one grouping type. A query’s filter can consist of any number of media property predicates. You build filters using [`MPMediaPropertyPredicate`](mpmediapropertypredicate.md) objects, based on property keys described in [`MPMediaItem`](mpmediaitem.md).

After creating and configuring a query, you use it to retrieve media items or media item collections. You can also use a query to retrieve an array of [`MPMediaQuerySection`](mpmediaquerysection.md) instances, useful for displaying the results of a query in the user interface of your app. See the [`itemSections`](mpmediaquery/itemsections.md) and [`collectionSections`](mpmediaquery/collectionsections.md) properties.

This class includes several convenience constructors that each apply a grouping type and, in most cases, match a subset of the library. The following table summarizes the features of these constructors. See [`MPMediaItem`](mpmediaitem.md) for descriptions of the entries in the Filter column. See [`MPMediaGrouping`](mpmediagrouping.md) for descriptions of the entries in the Grouping type column.

| Constructor name | Matches entire library | Filter | Grouping type |
| --- | --- | --- | --- |
| [`albums()`](mpmediaquery/albums().md) | - | [`music`](mpmediatype/music.md) | [`MPMediaGrouping.album`](mpmediagrouping/album.md) |
| [`artists()`](mpmediaquery/artists().md) | - | [`music`](mpmediatype/music.md) | [`MPMediaGrouping.artist`](mpmediagrouping/artist.md) |
| [`audiobooks()`](mpmediaquery/audiobooks().md) | - | [`audioBook`](mpmediatype/audiobook.md) | [`MPMediaGrouping.title`](mpmediagrouping/title.md) |
| [`compilations()`](mpmediaquery/compilations().md) | - | [`any`](mpmediatype/any.md) with [`MPMediaItemPropertyIsCompilation`](mpmediaitempropertyiscompilation.md) | [`MPMediaGrouping.album`](mpmediagrouping/album.md) |
| [`composers()`](mpmediaquery/composers().md) | Yes | [`any`](mpmediatype/any.md) | [`MPMediaGrouping.composer`](mpmediagrouping/composer.md) |
| [`genres()`](mpmediaquery/genres().md) | Yes | [`any`](mpmediatype/any.md) | [`MPMediaGrouping.genre`](mpmediagrouping/genre.md) |
| [`playlists()`](mpmediaquery/playlists().md) | Yes | [`any`](mpmediatype/any.md) | [`MPMediaGrouping.playlist`](mpmediagrouping/playlist.md) |
| [`podcasts()`](mpmediaquery/podcasts().md) | - | [`podcast`](mpmediatype/podcast.md) | [`MPMediaGrouping.podcastTitle`](mpmediagrouping/podcasttitle.md) |
| [`songs()`](mpmediaquery/songs().md) | - | [`music`](mpmediatype/music.md) | [`MPMediaGrouping.title`](mpmediagrouping/title.md) |

## Topics

### Creating media queries
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
- [init(filterPredicates: Set<MPMediaPredicate>?)](mpmediaquery/init(filterpredicates:).md)
  Initializes a media query with a set of media property predicates.
### Configuring media queries
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
- [enum MPMediaGrouping](mpmediagrouping.md)
  Keys used to configure a media query.
### Performing media queries
- [var items: [MPMediaItem]?](mpmediaquery/items.md)
  An array of media items that match the media query’s predicate.
- [var collections: [MPMediaItemCollection]?](mpmediaquery/collections.md)
  An array of media item collections whose contained items match the query’s media property predicate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Using filters to create specialized queries](using-filters-to-create-specialized-queries.md)
  Add a filter set to a query before populating a music player queue.
- [class MPMediaQuerySection](mpmediaquerysection.md)
  A range of media items or media item collections from within a media query.
- [class MPMediaPropertyPredicate](mpmediapropertypredicate.md)
  A set of predicates for defining a filter in a media query.
- [class MPMediaPredicate](mpmediapredicate.md)
  An abstract class that defines classes for filtering media in a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery)*