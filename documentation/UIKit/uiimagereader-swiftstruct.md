# UIImageReader

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct UIImageReader
```

## Topics

### Structures
- [UIImageReader.Configuration](uiimagereader-swift.struct/configuration-swift.struct.md)
  The properties that a reader uses to decode images.
### Initializers
- [init(configuration: UIImageReader.Configuration)](uiimagereader-swift.struct/init(configuration:).md)
### Instance Properties
- [var configuration: UIImageReader.Configuration](uiimagereader-swift.struct/configuration-swift.property.md)
### Instance Methods
- [func image(contentsOf: URL) async -> UIImage?](uiimagereader-swift.struct/image(contentsof:)-1p5sc.md)
- [func image(contentsOf: URL) -> UIImage?](uiimagereader-swift.struct/image(contentsof:)-94s2r.md)
- [func image(data: Data) async -> UIImage?](uiimagereader-swift.struct/image(data:)-5c16z.md)
- [func image(data: Data) -> UIImage?](uiimagereader-swift.struct/image(data:)-5gx82.md)
### Type Properties
- [static let `default`: UIImageReader](uiimagereader-swift.struct/default.md)

## See Also

- [init?(contentsOfFile: String)](uiimage/init(contentsoffile:).md)
  Initializes and returns the image object with the contents of the specified file.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct)*