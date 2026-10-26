# ar_error_copy_cf_error

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Copies a reference to a Core Foundation error object that represents the specified ARKit error.

**Availability**:
- visionOS 1.0+

## Declaration

```c
extern CFErrorRefar_error_copy_cf_error(ar_error_t error);
```

## See Also

### Errors
- [ar_error_t](./ar_error_t.md)
  An error reported by ARKit.
- [ar_error_code_t](./ar_error_code_t.md)
  Codes that identify errors in ARKit.
- [ar_error_domain](./ar_error_domain.md)
  A string that indicates the error domain in Core Foundation.
- [ar_error_get_error_code](./ar_error_get_error_code.md)
  Gets the error code associated with an error.
- [AR_EXTERN_C_BEGIN](./ar_extern_c_begin.md)
- [AR_EXTERN_C_END](./ar_extern_c_end.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_error_copy_cf_error)*