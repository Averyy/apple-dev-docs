# ar_error_copy_cf_error

**Framework**: ARKit  
**Kind**: func

Copies a reference to a Core Foundation error object that represents the specified ARKit error.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
extern CFErrorRef ar_error_copy_cf_error(ar_error_t error);
```

## See Also

- [ar_error_t](ar_error_t.md)
  An error reported by ARKit.
- [ar_error_code_t](ar_error_code_t.md)
  Codes that identify errors in ARKit.
- [ar_error_domain](ar_error_domain.md)
  A string that indicates the error domain in Core Foundation.
- [ar_error_get_error_code](ar_error_get_error_code.md)
  Gets the error code associated with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_error_copy_cf_error)*