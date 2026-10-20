# isExplicitContent

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, getter=isExplicitContent) BOOL explicitContent;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the designated content item’s identified as containing explicit content.

## See Also

### Retrieving information about a media item
- [var artwork: MPMediaItemArtwork?](./artwork.md)
  A single image that’s associated with the media item.
- [var isContainer: Bool](./iscontainer.md)
  A Boolean value that indicates whether a media item is container of other items.
- [var identifier: String](./identifier.md)
  The unique identifier for the media item.
- [var isPlayable: Bool](./isplayable.md)
  A Boolean value that indicates whether a media item is able to be played.
- [var isStreamingContent: Bool](./isstreamingcontent.md)
  A Boolean value that indicates whether the content item is streaming content.
- [var playbackProgress: Float](./playbackprogress.md)
  The amount of content played for the media item.
- [var subtitle: String?](./subtitle.md)
  A secondary designator for the media item.
- [var title: String?](./title.md)
  The public name of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/isexplicitcontent)*