# MediaSearch

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A description of the media items the user wants to play, add to a playlist, or express a preference for.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object MediaSearch
```

#### Discussion

A `releaseDate` may refer to the publication of a specific media item, or to music typical of a particular decade. For example, the client represents *Play some 80s music* with a `releaseDate` ranging from the first moment of 1980 to the last moment of 1989.

## Topics

### Prioritizing Search Results
- [type MediaSortOrder](mediasortorder.md)
  A prioritization for search results.
### Filtering by Release Date
- [object DateComponentsRange](datecomponentsrange.md)
  A period of time from a specified start date to a specified end date.
- [type DateComponents](datecomponents.md)
  A full or partial date and time.
- [object ExplicitDateComponents](explicitdatecomponents.md)
  A date or time in specified of units (such as year, month, day, hour, and minute) for evaluation in a calendar system and time zone.

## Properties

- `mediaName` (string): The name of the media item.
- `artistName` (string): The creator or performer of the media item.
- `albumName` (string): The album that contains the media item.
- `mediaType` (MediaItemType): The type of media the user wants.
- `genreNames` ([string]): Genres that apply to this media item. These are the same genres as those at [`genreNames`](https://developer.apple.com/documentation/intents/inmediasearch/genrenames).
- `moodNames` ([string]): Feelings that describe the media item the user wants, such as `happy` or `focused`.
- `releaseDate` (DateComponentsRange): The date of the media item’s first publication, or a period of time.
- `sortOrder` (MediaSortOrder): The prioritization to apply to search results.
- `reference` (MediaReference): An indicator of whether the client is playing this media item.
- `mediaIdentifier` (string): The identifier for a specific media item.

## See Also

- [object MediaItem](mediaitem.md)
  A particular piece of media that an intent references, such as a song, podcast episode, or playlist.
- [type MediaReference](mediareference.md)
  A way of identifying the current media item rather than with metadata.
- [type MediaItemType](mediaitemtype.md)
  Types of media items or media searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/mediasearch)*