# isExplicitContent

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether the media item contains explicit content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isExplicitContent: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the designated content item’s identified as containing explicit content.

## See Also

- [var artwork: MPMediaItemArtwork?](mpcontentitem/artwork.md)
  A single image that’s associated with the media item.
- [var isContainer: Bool](mpcontentitem/iscontainer.md)
  A Boolean value that indicates whether a media item is container of other items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/isexplicitcontent)*