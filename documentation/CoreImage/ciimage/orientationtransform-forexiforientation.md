# orientationTransform(forExifOrientation:)

**Framework**: Core Image  
**Kind**: method

Returns the transformation needed to reorient the image to the specified orientation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func orientationTransform(forExifOrientation orientation: Int32) -> CGAffineTransform
```

#### Return Value

An affine transform that will rotate or mirror the image to match the specified orientation when applied.

#### Discussion

This method determines the transformation needed to match the specified orientation, but does not apply that transformation to the image. To apply the transformation (possibly after concatenating it with other transformations), use the [`transformed(by:)`](ciimage/transformed(by:).md) method or the `CIAffineTransform` filter. To determine and apply the transformation in a single step, use the [`oriented(forExifOrientation:)`](ciimage/oriented(forexiforientation:).md) method.

## Parameters

- `orientation`: An integer specifying an image orientation according to the EXIF specification. For details, see  .

## See Also

- [var definition: CIFilterShape](ciimage/definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](ciimage/properties.md)
  Returns the metadata properties dictionary of the image.
- [var url: URL?](ciimage/url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/colorspace.md)
  The color space of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/orientationtransform(forexiforientation:))*