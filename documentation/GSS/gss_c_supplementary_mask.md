# GSS_C_SUPPLEMENTARY_MASK

**Framework**: GSS  
**Kind**: var

A mask with a width that matches the supplementary information field.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var GSS_C_SUPPLEMENTARY_MASK: UInt { get }
```

#### Discussion

Shift the mask to the left by [`GSS_C_SUPPLEMENTARY_OFFSET`](gss_c_supplementary_offset.md) to put it in the correct position within the major status code to match the supplementary information field. The [`GSS_SUPPLEMENTARY_INFO`](gss_supplementary_info.md) macro does this for you, before bitwise `AND`ing with its input.

## See Also

- [var GSS_C_CALLING_ERROR_MASK: UInt](gss_c_calling_error_mask.md)
  A mask with a width that matches the calling error field.
- [var GSS_C_CALLING_ERROR_OFFSET: Int32](gss_c_calling_error_offset.md)
  The offset of the calling error field within the major status code.
- [var GSS_C_ROUTINE_ERROR_MASK: UInt](gss_c_routine_error_mask.md)
  A mask with a width that matches the routine error field.
- [var GSS_C_ROUTINE_ERROR_OFFSET: Int32](gss_c_routine_error_offset.md)
  The offset of the routine error field within the major status code.
- [var GSS_C_SUPPLEMENTARY_OFFSET: Int32](gss_c_supplementary_offset.md)
  The offset of the supplementary information field within the major status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_c_supplementary_mask)*