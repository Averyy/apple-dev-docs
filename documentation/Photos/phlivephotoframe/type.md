# type

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The type of image content in this frame.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var type: PHLivePhotoFrameType { get }
```

```objc
@property (nonatomic, readonly) PHLivePhotoFrameType type;
```

#### Discussion

Photos calls your [`frameProcessor`](../phlivephotoeditingcontext/frameprocessor.md) block repeatedly, both to process each frame of the Live Photo’s video content and to process the Live Photo’s still photo content. Use this property to distinguish photo content from video frames—for example, to add a watermark only to still photo content.

## See Also

### Getting Information About the Frame
- [var renderScale: CGFloat](./renderscale.md)
  The scale factor of the frame image relative to the Live Photo’s photo content.
- [var time: CMTime](./time.md)
  The time offset, in seconds, of this frame relative to the start of the Live Photo.
- [enum PHLivePhotoFrameType](../phlivephotoframetype.md)
  Identifiers for the type of frame image to be processed. Used with the [`type`](./type.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoframe/type)*