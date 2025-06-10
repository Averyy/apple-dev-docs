# MPMediaItemAnimatedArtwork

**Framework**: Media Player  
**Kind**: class

An animated image, such as an animated music album cover art, for a media item.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class MPMediaItemAnimatedArtwork
```

#### Overview

A single instance of animated artwork is comprised of two assets: an artwork video asset, and a preview image which should match the first frame of the artwork video. The preview image may be used when displaying the animated artwork whilst the video becomes available.

Both the preview image and artwork video can be fetched asynchronously and will only be requested when required at point of display. Aim to provide preview images as quickly as possible once requested, and ideally synchronously.

Video asset `URL`s you provide must be local file `URL`s. You should make the associated assets available locally before providing them via the relevant handler, for example by fetching the associated video asset over the network. The `URL`s should remain valid for the lifetime of the [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md), once provided.

[`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) should not be subclassed.

## Topics

### Initializers
- [convenience init(artworkID: String, previewImageRequestHandler: (CGSize) async -> UIImage?, videoAssetFileURLRequestHandler: (CGSize) async -> URL?)](mpmediaitemanimatedartwork/init(artworkid:previewimagerequesthandler:videoassetfileurlrequesthandler:)-7bb3j.md)
  Creates an animated artwork.
- [convenience init(artworkID: String, previewImageRequestHandler: (CGSize) async -> NSImage?, videoAssetFileURLRequestHandler: (CGSize) async -> URL?)](mpmediaitemanimatedartwork/init(artworkid:previewimagerequesthandler:videoassetfileurlrequesthandler:)-7n23z.md)
  Creates an animated artwork.
- [init(artworkID: String, previewImageRequestHandler: (CGSize, (UIImage?) -> Void) -> Void, videoAssetFileURLRequestHandler: (CGSize, (URL?) -> Void) -> Void)](mpmediaitemanimatedartwork/init(artworkid:previewimagerequesthandler:videoassetfileurlrequesthandler:)-ieue.md)
  Creates an animated artwork.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPMediaItem](mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemanimatedartwork)*