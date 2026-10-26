# PHLivePhotoFrameType

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Identifiers for the type of frame image to be processed. Used with the [`type`](./phlivephotoframe/type.md) property.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHLivePhotoFrameType
```

```c
enum PHLivePhotoFrameType : NSInteger;
```

## Topics

### Constants
- [PHLivePhotoFrameType.photo](./phlivephotoframetype/photo.md)
  The image is a still photo.
- [PHLivePhotoFrameType.video](./phlivephotoframetype/video.md)
  The image is a single frame from the Live Photo’s video content.
### Initializers
- [init?(rawValue: Int)](./phlivephotoframetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Information About the Frame
- [var renderScale: CGFloat](./phlivephotoframe/renderscale.md)
  The scale factor of the frame image relative to the Live Photo’s photo content.
- [var time: CMTime](./phlivephotoframe/time.md)
  The time offset, in seconds, of this frame relative to the start of the Live Photo.
- [var type: PHLivePhotoFrameType](./phlivephotoframe/type.md)
  The type of image content in this frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoframetype)*