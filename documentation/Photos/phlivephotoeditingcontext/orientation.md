# orientation

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The image orientation of the Live Photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var orientation: CGImagePropertyOrientation { get }
```

```objc
@property (readonly) CGImagePropertyOrientation orientation;
```

## Discussion

This [`fullSizeImage`](./fullsizeimage.md) object does not reflect the Live Photo’s orientation metadata. Use this property when displaying that image to ensure that it appears to the user in the correct orientation.

## See Also

### Examining an Editing Context’s Live Photo
- [var fullSizeImage: CIImage](./fullsizeimage.md)
  The unedited still photo content of the Live Photo.
- [var duration: CMTime](./duration.md)
  The duration, in seconds, of the Live Photo.
- [var photoTime: CMTime](./phototime.md)
  The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/orientation)*