# IMAGEIO_PNG_NO_FILTERS

**Framework**: Image I/O  
**Kind**: var

No PNG filters.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var IMAGEIO_PNG_NO_FILTERS: Int32 { get }
```

## See Also

- [let kCGImagePropertyPNGCompressionFilter: CFString](kcgimagepropertypngcompressionfilter.md)
  The PNG filter to apply prior to compression.
- [var IMAGEIO_PNG_FILTER_NONE: Int32](imageio_png_filter_none.md)
  A filter in which each byte is unchanged.
- [var IMAGEIO_PNG_FILTER_SUB: Int32](imageio_png_filter_sub.md)
  A filter in which each byte is replaced with the difference between it and the corresponding byte to its left.
- [var IMAGEIO_PNG_FILTER_UP: Int32](imageio_png_filter_up.md)
  A filter in which each byte is replaced with the difference between it and the byte above it.
- [var IMAGEIO_PNG_FILTER_AVG: Int32](imageio_png_filter_avg.md)
  A filter in which each byte is replaced with the difference between it and the average of the bytes above it and to its left.
- [var IMAGEIO_PNG_FILTER_PAETH: Int32](imageio_png_filter_paeth.md)
  A filter in which each byte is replaced with the difference between it and the Paeth predictor of the bytes to its left, above, and upper left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/imageio_png_no_filters)*