# kCGImagePropertyPNGCompressionFilter

**Framework**: Image I/O  
**Kind**: var

The PNG filter to apply prior to compression.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImagePropertyPNGCompressionFilter: CFString
```

#### Discussion

The value of this key is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber). The number contains a bitwise-OR of one or more filter constants, such as [`IMAGEIO_PNG_FILTER_AVG`](imageio_png_filter_avg.md) or [`IMAGEIO_PNG_FILTER_SUB`](imageio_png_filter_sub.md). The value has no effect on formats other than PNG.

## See Also

- [var IMAGEIO_PNG_NO_FILTERS: Int32](imageio_png_no_filters.md)
  No PNG filters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcompressionfilter)*