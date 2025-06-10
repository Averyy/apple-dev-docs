# kvImage_PNG_FILTER_VALUE_AVG

**Framework**: Accelerate  
**Kind**: var

A filter that predicts a pixel value from the average of the pixels to the left and above the predicted pixel location.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kvImage_PNG_FILTER_VALUE_AVG: Int { get }
```

## See Also

- [var kvImage_PNG_FILTER_VALUE_NONE: Int](kvimage_png_filter_value_none.md)
  No filtering.
- [var kvImage_PNG_FILTER_VALUE_SUB: Int](kvimage_png_filter_value_sub.md)
  A filter that computes the difference between each byte of a pixel and the value of the corresponding byte of the pixel located to the left.
- [var kvImage_PNG_FILTER_VALUE_UP: Int](kvimage_png_filter_value_up.md)
  A filter that computes the difference between each byte of a pixel and the value of the corresponding byte of the pixel located above.
- [var kvImage_PNG_FILTER_VALUE_PAETH: Int](kvimage_png_filter_value_paeth.md)
  A filter that predicts a pixel value by applying a linear function to the pixels located to the left, above, and to the upper-left of the predicted pixel location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimage_png_filter_value_avg)*