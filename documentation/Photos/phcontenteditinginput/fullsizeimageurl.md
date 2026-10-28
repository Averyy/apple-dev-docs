# fullSizeImageURL

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The URL to a file that contains the full-sized image data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fullSizeImageURL: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * fullSizeImageURL;
```

## Discussion

Typically, your app or extension does not need to load a full-sized image for use in an editing UI. Instead, use the [`displaySizeImage`](./displaysizeimage.md) property to retrieve an image suitable for screen display. You can then load the full-sized image on a background queue so that it will be ready by the time the user finishes editing the display-size image. At that time, apply the user’s adjustments to the full-sized image and then use the [`PHContentEditingOutput`](../phcontenteditingoutput.md) class to commit the edit to the photo library.

## See Also

### Working with Photo Assets
- [var displaySizeImage: UIImage?](./displaysizeimage.md)
  An image of the asset’s contents, appropriately sized for display.
- [var fullSizeImageOrientation: Int32](./fullsizeimageorientation.md)
  The Exif display orientation of the full-size image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/fullsizeimageurl)*