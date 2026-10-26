# fullSizeImage

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The unedited still photo content of the Live Photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fullSizeImage: CIImage { get }
```

```objc
@property (readonly) CIImage * fullSizeImage;
```

#### Discussion

Use this property to display the unedited Live Photo’s photo content, or to provide still-image previews in your editing UI.

> **Note**:  For the best interactive editing performance, use a Metal, OpenGL, or OpenGL ES view and corresponding Core Image context to render editing results. See [Processing Images](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_tasks/ci_tasks.html#//apple_ref/doc/uid/TP30001185-CH3) in [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for details and examples.

This image does not reflect the Live Photo’s orientation metadata. Adjust your rendering based on the [`orientation`](./orientation.md) property to ensure that the image appears to the user in the correct orientation.

## See Also

### Examining an Editing Context’s Live Photo
- [var duration: CMTime](./duration.md)
  The duration, in seconds, of the Live Photo.
- [var photoTime: CMTime](./phototime.md)
  The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.
- [var orientation: CGImagePropertyOrientation](./orientation.md)
  The image orientation of the Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/fullsizeimage)*