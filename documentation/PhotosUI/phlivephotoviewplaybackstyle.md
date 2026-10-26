# PHLivePhotoViewPlaybackStyle

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Options for how much of the motion and sound content of a Live Photo to play, used in the [`startPlayback(with:)`](./phlivephotoview/startplayback%28with%29.md) method and in messages to the view’s [`delegate`](./phlivephotoview/delegate.md) object.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHLivePhotoViewPlaybackStyle
```

```c
enum PHLivePhotoViewPlaybackStyle : NSInteger;
```

## Topics

### Constants
- [PHLivePhotoViewPlaybackStyle.undefined](./phlivephotoviewplaybackstyle/undefined.md)
  This value is invalid for use.
- [PHLivePhotoViewPlaybackStyle.full](./phlivephotoviewplaybackstyle/full.md)
  Plays back the entire motion and sound content of the Live Photo, including transition effects at the start and end.
- [PHLivePhotoViewPlaybackStyle.hint](./phlivephotoviewplaybackstyle/hint.md)
  Plays back only a brief section of the motion content of the Live Photo, without sound.
### Initializers
- [init?(rawValue: Int)](./phlivephotoviewplaybackstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct PHLivePhotoBadgeOptions](./phlivephotobadgeoptions.md)
  Options for the semantic use and display style of icons for badging Live Photo assets, used by the [`livePhotoBadgeImage(options:)`](./phlivephotoview/livephotobadgeimage%28options%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoviewplaybackstyle)*