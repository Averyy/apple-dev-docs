# MediaReference

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

A way of identifying the current media item rather than with metadata.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string MediaReference
```

## Possible Values

- `currentlyPlaying`: The media item the device is playing.
- `unknown`: An unspecified reference.
- `my`: Information specific to the user, as in *Play my Top 10 playlist*.

## See Also

### Media Items
- [object MediaItem](./mediaitem.md)
  A particular piece of media that an intent references, such as a song, podcast episode, or playlist.
- [object MediaSearch](./mediasearch.md)
  A description of the media items the user wants to play, add to a playlist, or express a preference for.
- [type MediaItemType](./mediaitemtype.md)
  Types of media items or media searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/mediareference)*