# properties

**Framework**: Core Image  
**Kind**: property

Returns the metadata properties dictionary of the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var properties: [String : Any] { get }
```

#### Discussion

If the [`CIImage`](ciimage.md) was created from `NSURL` or `NSData` then this dictionary is determined by calling `CGImageSourceCopyPropertiesAtIndex()`.

If the [`CIImage`](ciimage.md) was created with the [`properties`](ciimageoption/properties.md) option, then that dictionary is returned.

If the [`CIImage`](ciimage.md) was created by applying [`CIFilter`](cifilter-swift.class.md) or [`CIKernel`](cikernel.md) then the properties of the root inputImage will be returned.

## See Also

- [var definition: CIFilterShape](ciimage/definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/extent.md)
  A rectangle that specifies the extent of the image.
- [var url: URL?](ciimage/url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/orientationtransform(forexiforientation:).md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/properties)*