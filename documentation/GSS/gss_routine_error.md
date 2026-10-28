# GSS_ROUTINE_ERROR

**Framework**: GSS  
**Kind**: macro  
**Role**: Macro

A macro that masks out all but the routine error field from a major status code.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```c
#define GSS_ROUTINE_ERROR(x)
```

## Discussion

Apply this macro to a major status code, then compare the result with one of the routine error constants to determine which calling error occurred.

## See Also

### Extraction Macros
- [GSS_ERROR](./gss_error.md)
  A macro that masks the supplementary info out of a major status code, leaving both calling and routine error fields.
- [GSS_CALLING_ERROR](./gss_calling_error.md)
  A macro that masks out all but the calling error field from a major status code.
- [GSS_SUPPLEMENTARY_INFO](./gss_supplementary_info.md)
  A macro that masks out all but the supplementary information field from a major status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_routine_error)*