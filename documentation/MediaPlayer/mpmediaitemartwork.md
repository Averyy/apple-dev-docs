# MPMediaItemArtwork

**Framework**: Media Player  
**Kind**: class

A graphical image, such as music album cover art, associated with a media item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPMediaItemArtwork
```

## Topics

### Resizing existing artwork
- [init(boundsSize: CGSize, requestHandler: (CGSize) -> UIImage)](mpmediaitemartwork/init(boundssize:requesthandler:).md)
  Creates a new image from existing artwork with the specified bounds.
### Using a media item image
- [func image(at: CGSize) -> UIImage?](mpmediaitemartwork/image(at:).md)
  Returns the artwork image for an item at the given size.
- [var bounds: CGRect](mpmediaitemartwork/bounds.md)
  The maximum size, in points, of the image associated with the media item artwork.
### Initializers
- [convenience init(image: UIImage)](mpmediaitemartwork/init(image:).md)
  Initializes a media item artwork instance with a full-size image.
### Instance Properties
- [var imageCropRect: CGRect](mpmediaitemartwork/imagecroprect.md)
  The bounds, in points, of the content area for the full size image associated with the media item artwork.

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
- [class MPMediaItemAnimatedArtwork](mpmediaitemanimatedartwork.md)
  An animated image, such as an animated music album cover art, for a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork)*