# isPlayable

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a media item is able to be played.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+

## Declaration

```swift
var isPlayable: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isPlayable) BOOL playable;
```

## Discussion

When set to [`true`](../../Swift/true.md), the designated content item is able to be played. Containers and individual content items can set this property to [`true`](../../Swift/true.md). For example, a playlist with multiple songs in it. The playlist is a container that can be played, or the user could choose a song from inside of the playlist.

## See Also

### Retrieving information about a media item
- [var artwork: MPMediaItemArtwork?](./artwork.md)
  A single image that’s associated with the media item.
- [var isContainer: Bool](./iscontainer.md)
  A Boolean value that indicates whether a media item is container of other items.
- [var isExplicitContent: Bool](./isexplicitcontent.md)
  A Boolean value that indicates whether the media item contains explicit content.
- [var identifier: String](./identifier.md)
  The unique identifier for the media item.
- [var isStreamingContent: Bool](./isstreamingcontent.md)
  A Boolean value that indicates whether the content item is streaming content.
- [var playbackProgress: Float](./playbackprogress.md)
  The amount of content played for the media item.
- [var subtitle: String?](./subtitle.md)
  A secondary designator for the media item.
- [var title: String?](./title.md)
  The public name of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/isplayable)*