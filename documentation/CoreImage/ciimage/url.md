# url

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The URL from which the image was loaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (atomic, readonly, nullable) NSURL * url;
```

#### Discussion

A URL is available only if the image object was created with a URL (such as with the [`init(contentsOf:)`](./init%28contentsof%29.md) method or related methods). Otherwise, this property’s value is `nil`.

## See Also

### Getting Image Information
- [var definition: CIFilterShape](./definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](./extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](./properties.md)
  Returns the metadata properties dictionary of the image.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](./orientationtransform%28forexiforientation%29.md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/url)*