# artwork

**Framework**: Media Player  
**Kind**: property

A single image that’s associated with the media item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+

## Declaration

```swift
var artwork: MPMediaItemArtwork? { get set }
```

#### Discussion

An image that’s displayed with the media item. A song would have an album cover image, whereas a movie could have a movie poster image associated with it.

## See Also

- [var isContainer: Bool](mpcontentitem/iscontainer.md)
  A Boolean value that indicates whether a media item is container of other items.
- [var isExplicitContent: Bool](mpcontentitem/isexplicitcontent.md)
  A Boolean value that indicates whether the media item contains explicit content.
- [var identifier: String](mpcontentitem/identifier.md)
  The unique identifier for the media item.
- [var isPlayable: Bool](mpcontentitem/isplayable.md)
  A Boolean value that indicates whether a media item is able to be played.
- [var isStreamingContent: Bool](mpcontentitem/isstreamingcontent.md)
  A Boolean value that indicates whether the content item is streaming content.
- [var playbackProgress: Float](mpcontentitem/playbackprogress.md)
  The amount of content played for the media item.
- [var subtitle: String?](mpcontentitem/subtitle.md)
  A secondary designator for the media item.
- [var title: String?](mpcontentitem/title.md)
  The public name of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/artwork)*