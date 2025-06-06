# playbackProgress

**Framework**: Media Player  
**Kind**: property

The amount of content played for the media item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+

## Declaration

```swift
var playbackProgress: Float { get set }
```

#### Discussion

The value of this property ranges from `0.0` to `1.0`. A value `0.0` indicates that the media item hasn’t played, while `1.0` indicates that the media item has completely played. The default value is `–1.0` indicates that the progress indicator isn’t displayed. The system displays a progress indicator automatically if this property has a value between `0.0` and `1.0`.

## See Also

- [var artwork: MPMediaItemArtwork?](mpcontentitem/artwork.md)
  A single image that’s associated with the media item.
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
- [var subtitle: String?](mpcontentitem/subtitle.md)
  A secondary designator for the media item.
- [var title: String?](mpcontentitem/title.md)
  The public name of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/playbackprogress)*