# GSS_IOV_BUFFER_TYPE_FLAG_MASK

**Framework**: GSS  
**Kind**: var

The buffer type is a flag mask.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var GSS_IOV_BUFFER_TYPE_FLAG_MASK: UInt32 { get }
```

## See Also

- [var GSS_IOV_BUFFER_FLAG_ALLOCATE: Int32](gss_iov_buffer_flag_allocate.md)
  GSS should perform the allocation.
- [var GSS_IOV_BUFFER_FLAG_ALLOCATED: Int32](gss_iov_buffer_flag_allocated.md)
  The caller should free the buffer.
- [var GSS_IOV_BUFFER_TYPE_DATA: Int32](gss_iov_buffer_type_data.md)
  The buffer type is packet data.
- [var GSS_IOV_BUFFER_TYPE_EMPTY: Int32](gss_iov_buffer_type_empty.md)
  The buffer type is empty.
- [var GSS_IOV_BUFFER_TYPE_FLAG_ALLOCATE: Int32](gss_iov_buffer_type_flag_allocate.md)
  GSS should perform the allocation.
- [var GSS_IOV_BUFFER_TYPE_FLAG_ALLOCATED: Int32](gss_iov_buffer_type_flag_allocated.md)
  The caller should free the buffer.
- [var GSS_IOV_BUFFER_TYPE_HEADER: Int32](gss_iov_buffer_type_header.md)
  The buffer type is a mechanism header.
- [var GSS_IOV_BUFFER_TYPE_MECH_PARAMS: Int32](gss_iov_buffer_type_mech_params.md)
  The buffer contains mechanism-specific parameters.
- [var GSS_IOV_BUFFER_TYPE_PADDING: Int32](gss_iov_buffer_type_padding.md)
  The buffer contains padding.
- [var GSS_IOV_BUFFER_TYPE_SIGN_ONLY: Int32](gss_iov_buffer_type_sign_only.md)
  The buffer contains sign-only packet data.
- [var GSS_IOV_BUFFER_TYPE_STREAM: Int32](gss_iov_buffer_type_stream.md)
  The buffer contains a complete wrap token.
- [var GSS_IOV_BUFFER_TYPE_TRAILER: Int32](gss_iov_buffer_type_trailer.md)
  The buffer contains a mechanism trailer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_iov_buffer_type_flag_mask)*