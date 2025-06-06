# Using filters to create specialized queries

**Framework**: Media Player

Add a filter set to a query before populating a music player queue.

#### Overview

Creating a queue and adding it to a music player is a straightforward task. You populate the music player queue by creating a basic query and searching the user’s music library for items that match the query. However, you can create filters and add them at query creation to refine the player’s music queue. Filter for an album, artist, song, or any of a variety of other options. For a list of keys you can use as filters, see [`General media item property keys`](general-media-item-property-keys.md).

##### Create One or More Filters

You need to create a new filter for each item you want to filter on. For example, if you want to filter for a specific album and all songs that contain a certain word from that album, you need two separate filters.

```swift
let albumTitleFilter =
    MPMediaPropertyPredicate(value: "Album Title",
                             forProperty: MPMediaItemPropertyAlbumTitle,
                             comparisonType: .equalTo)

let songTitleFilter =
    MPMediaPropertyPredicate(value: "Song Title",
                             forProperty: MPMediaItemPropertyTitle,
                             comparisonType: .contains)
```

##### Combine the Filters Into a Filter Set

Combine the filters into a filter set before you assign it to a query.

```swift
let filterSet = Set([albumTitleFilter, songTitleFilter])
```

##### Create a Query Using the Filter Set

Create a new query using the newly created filter set, and set the music player’s queue.

```swift
let query = MPMediaQuery(filterPredicates: filterSet)
musicPlayer.setQueue(with: query)
```

## See Also

- [class MPMediaQuery](mpmediaquery.md)
  A query that specifies a set of media items from the device’s media library using a filter and a grouping type.
- [class MPMediaQuerySection](mpmediaquerysection.md)
  A range of media items or media item collections from within a media query.
- [class MPMediaPropertyPredicate](mpmediapropertypredicate.md)
  A set of predicates for defining a filter in a media query.
- [class MPMediaPredicate](mpmediapredicate.md)
  An abstract class that defines classes for filtering media in a media query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/using-filters-to-create-specialized-queries)*