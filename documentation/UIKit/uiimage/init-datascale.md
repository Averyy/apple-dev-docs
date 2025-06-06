# init(data:scale:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns the image object with the specified data and scale factor.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(data: Data, scale: CGFloat)
```

#### Return Value

An initialized `UIImage` object, or `nil` if the method could not initialize the image from the specified data.

#### Discussion

The data in the `data` parameter must be formatted to match the file format of one of the system’s supported image types.

## Parameters

- `data`: The data object containing the image data.
- `scale`: The scale factor to assume when interpreting the image data. Applying a scale factor of 1.0 results in an image whose size matches the pixel-based dimensions of the image. Applying a different scale factor changes the size of the image as reported by the   property.

## See Also

- [init?(contentsOfFile: String)](uiimage/init(contentsoffile:).md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](uiimage/init(data:).md)
  Initializes and returns the image object with the specified data.
- [init(cgImage: CGImage)](uiimage/init(cgimage:).md)
  Initializes and returns the image object with the specified Quartz image reference.
- [init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(cgimage:scale:orientation:).md)
  Initializes and returns an image object with the specified scale and orientation factors.
- [init(ciImage: CIImage)](uiimage/init(ciimage:).md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(ciimage:scale:orientation:).md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [struct UIImageReader](uiimagereader-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(data:scale:))*