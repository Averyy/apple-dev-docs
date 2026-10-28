# colorSpace

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The color space of the image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var colorSpace: CGColorSpace? { get }
```

```objc
@property (atomic, readonly, nullable) CGColorSpaceRef colorSpace;
```

## Discussion

This property’s value is `nil` if the image’s color space cannot be determined.

## See Also

### Getting Image Information
- [var definition: CIFilterShape](./definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](./extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](./properties.md)
  Returns the metadata properties dictionary of the image.
- [var url: URL?](./url.md)
  The URL from which the image was loaded.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](./orientationtransform%28forexiforientation%29.md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/colorspace)*