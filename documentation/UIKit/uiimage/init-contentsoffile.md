# init(contentsOfFile:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns the image object with the contents of the specified file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(contentsOfFile path: String)
```

#### Return Value

An initialized `UIImage` object, or `nil` if the method could not find the file or initialize the image from its contents.

#### Discussion

This method loads the image data into memory and marks it as purgeable. If the data is purged and needs to be reloaded, the image object loads that data again from the specified path.

## Parameters

- `path`: The path to the file. This path should include the filename extension that identifies the type of the image data.

## See Also

- [init?(data: Data)](uiimage/init(data:).md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](uiimage/init(data:scale:).md)
  Initializes and returns the image object with the specified data and scale factor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(contentsoffile:))*