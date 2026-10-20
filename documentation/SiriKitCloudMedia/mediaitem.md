# MediaItem

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A particular piece of media that an intent references, such as a song, podcast episode, or playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object MediaItem
```

## Properties

- `identifier` (string) *(required)*: An identifier for the media item that’s stable within the [`Session`](./session.md) and unique among all media of this `type` within this `Session`.

  **Maximum Length**: `250`
- `title` (string): The name of this media item.

  **Maximum Length**: `1000`
- `artist` (string): The performer of this media item.

  **Maximum Length**: `1000`
- `type` (MediaItemType) *(required)*: The media item’s type.

## See Also

### Media Items
- [type MediaReference](./mediareference.md)
  A way of identifying the current media item rather than with metadata.
- [object MediaSearch](./mediasearch.md)
  A description of the media items the user wants to play, add to a playlist, or express a preference for.
- [type MediaItemType](./mediaitemtype.md)
  Types of media items or media searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/mediaitem)*