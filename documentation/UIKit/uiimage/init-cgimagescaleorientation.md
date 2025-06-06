# init(cgImage:scale:orientation:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns an image object with the specified scale and orientation factors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)
```

#### Return Value

An initialized `UIImage` object. In Objective-C, this method returns `nil` if the `ciImage` parameter is `nil`.

## Parameters

- `cgImage`: The Quartz image object.
- `scale`: The scale factor to assume when interpreting the image data. Applying a scale factor of 1.0 results in an image whose size matches the pixel-based dimensions of the image. Applying a different scale factor changes the size of the image as reported by the   property.
- `orientation`: The orientation of the image data. You can use this parameter to specify any rotation factors applied to the image.

## See Also

- [init?(contentsOfFile: String)](uiimage/init(contentsoffile:).md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](uiimage/init(data:).md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](uiimage/init(data:scale:).md)
  Initializes and returns the image object with the specified data and scale factor.
- [init(cgImage: CGImage)](uiimage/init(cgimage:).md)
  Initializes and returns the image object with the specified Quartz image reference.
- [init(ciImage: CIImage)](uiimage/init(ciimage:).md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(ciimage:scale:orientation:).md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [struct UIImageReader](uiimagereader-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(cgimage:scale:orientation:))*