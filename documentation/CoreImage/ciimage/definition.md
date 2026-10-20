# definition

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Returns a filter shape object that represents the domain of definition of the image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var definition: CIFilterShape { get }
```

```objc
@property (atomic, readonly) CIFilterShape * definition;
```

#### Return Value

A filter shape object.

## See Also

### Getting Image Information
- [var extent: CGRect](./extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](./properties.md)
  Returns the metadata properties dictionary of the image.
- [var url: URL?](./url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](./orientationtransform%28forexiforientation%29.md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/definition)*