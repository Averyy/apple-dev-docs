# photoTime

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var photoTime: CMTime { get }
```

```objc
@property (readonly) CMTime photoTime;
```

## Discussion

To create time-based effects in your [`frameProcessor`](./frameprocessor.md) block, use this property together with the [`duration`](./duration.md) property.

## See Also

### Examining an Editing Context’s Live Photo
- [var fullSizeImage: CIImage](./fullsizeimage.md)
  The unedited still photo content of the Live Photo.
- [var duration: CMTime](./duration.md)
  The duration, in seconds, of the Live Photo.
- [var orientation: CGImagePropertyOrientation](./orientation.md)
  The image orientation of the Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/phototime)*