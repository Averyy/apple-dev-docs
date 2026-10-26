# fullSizeImageOrientation

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The Exif display orientation of the full-size image file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fullSizeImageOrientation: Int32 { get }
```

```objc
@property (assign, readonly) int fullSizeImageOrientation;
```

#### Discussion

This property’s value is a raw numeric value describing the encoded image orientation according to the TIFF and Exif specifications. To more easily work with such values, convert this value to the [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md) type.

## See Also

### Related Documentation
- [enum CGImagePropertyOrientation](../../ImageIO/cgimagepropertyorientation.md)
  A value describing the intended display orientation for an image.
### Working with Photo Assets
- [var displaySizeImage: UIImage?](./displaysizeimage.md)
  An image of the asset’s contents, appropriately sized for display.
- [var fullSizeImageURL: URL?](./fullsizeimageurl.md)
  The URL to a file that contains the full-sized image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/fullsizeimageorientation)*