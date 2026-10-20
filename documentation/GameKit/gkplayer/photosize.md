# GKPlayer.PhotoSize

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The size of a photo that Game Center loads.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum PhotoSize
```

```c
enum GKPhotoSize : NSInteger;
```

## Topics

### Constants
- [GKPlayer.PhotoSize.small](./photosize/small.md)
  Loads a small photo.
- [GKPlayer.PhotoSize.normal](./photosize/normal.md)
  Loads a normal-sized photo.
### Initializers
- [init?(rawValue: Int)](./photosize/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Loading player photos
- [func loadPhoto(for: GKPlayer.PhotoSize, withCompletionHandler: ((UIImage?, (any Error)?) -> Void)?)](./loadphoto%28for,withcompletionhandler%29.md)
  Loads a photo of the player from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/photosize)*