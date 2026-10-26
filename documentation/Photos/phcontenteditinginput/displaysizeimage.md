# displaySizeImage

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An image of the asset’s contents, appropriately sized for display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var displaySizeImage: UIImage? { get }
```

*macOS*

```swift
var displaySizeImage: NSImage? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (strong, readonly, nullable) UIImage * displaySizeImage;
```

*macOS*

```objc
@property (strong, readonly, nullable) NSImage * displaySizeImage;
```

#### Discussion

This property does not provide the full-sized image for a photo asset but rather a scaled-down image appropriate for use in a photo editing user interface. To load the full-sized asset image, use the [`fullSizeImageURL`](./fullsizeimageurl.md) property.

## See Also

### Working with Photo Assets
- [var fullSizeImageOrientation: Int32](./fullsizeimageorientation.md)
  The Exif display orientation of the full-size image file.
- [var fullSizeImageURL: URL?](./fullsizeimageurl.md)
  The URL to a file that contains the full-sized image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/displaysizeimage)*