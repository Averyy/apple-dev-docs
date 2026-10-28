# GSS_ERROR

**Framework**: GSS  
**Kind**: macro  
**Role**: Macro

A macro that masks the supplementary info out of a major status code, leaving both calling and routine error fields.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```c
#define GSS_ERROR(x)
```

## Discussion

When you apply this macro to a major status code, a non-zero result indicates that an error of some kind occurred.

## See Also

### Extraction Macros
- [GSS_CALLING_ERROR](./gss_calling_error.md)
  A macro that masks out all but the calling error field from a major status code.
- [GSS_ROUTINE_ERROR](./gss_routine_error.md)
  A macro that masks out all but the routine error field from a major status code.
- [GSS_SUPPLEMENTARY_INFO](./gss_supplementary_info.md)
  A macro that masks out all but the supplementary information field from a major status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_error)*