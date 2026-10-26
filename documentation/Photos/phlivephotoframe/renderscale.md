# renderScale

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The scale factor of the frame image relative to the Live Photo’s photo content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var renderScale: CGFloat { get }
```

```objc
@property (readonly) CGFloat renderScale;
```

#### Discussion

Photos calls your [`frameProcessor`](../phlivephotoeditingcontext/frameprocessor.md) block repeatedly, both to process each frame of the Live Photo’s video content and to process the Live Photo’s still photo content. Video frames can be a different size than still photo content—use this value to scale any of your image processing parameters that depend on the image’s size.

For example, the following code uses this property to ensure that the radius of a blur filter is consistent across all frames of a Live Photo:

**Swift**:

```swift
 
context.frameProcessor = { frame, _ in
    // Apply a blur whose radius is 10 pixels in the photo, scaled accordingly for video frames.
    return frame.image.applyingGaussianBlur(withSigma: frame.renderScale * 10)
}
```

**Objective-C**:

```objc
context.frameProcessor = ^CIImage *(id <PHLivePhotoFrame> frame, NSError **error) {
    // Apply a blur whose radius is 10 pixels in the photo, scaled accordingly for video frames.
    return [frame.image imageByApplyingGaussianBlurWithRadius:(frame.renderScale * 10)];
};
```

## See Also

### Getting Information About the Frame
- [var time: CMTime](./time.md)
  The time offset, in seconds, of this frame relative to the start of the Live Photo.
- [var type: PHLivePhotoFrameType](./type.md)
  The type of image content in this frame.
- [enum PHLivePhotoFrameType](../phlivephotoframetype.md)
  Identifiers for the type of frame image to be processed. Used with the [`type`](./type.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoframe/renderscale)*