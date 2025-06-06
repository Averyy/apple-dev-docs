# init(cgImage:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns the image object with the specified Quartz image reference.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(cgImage: CGImage)
```

#### Return Value

An initialized `UIImage` object, or `nil` if the method could not initialize the image from the specified data.

## Parameters

- `cgImage`: A Quartz image reference.

## See Also

- [init?(contentsOfFile: String)](uiimage/init(contentsoffile:).md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](uiimage/init(data:).md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](uiimage/init(data:scale:).md)
  Initializes and returns the image object with the specified data and scale factor.
- [init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(cgimage:scale:orientation:).md)
  Initializes and returns an image object with the specified scale and orientation factors.
- [init(ciImage: CIImage)](uiimage/init(ciimage:).md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(ciimage:scale:orientation:).md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [struct UIImageReader](uiimagereader-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(cgimage:))*