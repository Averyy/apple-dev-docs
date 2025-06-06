# gss_iov_buffer_t

**Framework**: GSS  
**Kind**: typealias

The structure for a vectored I/O buffer and its defined type.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
typealias gss_iov_buffer_t = UnsafeMutablePointer<gss_iov_buffer_desc_struct>
```

## See Also

- [typealias gss_qop_t](gss_qop_t.md)
  A quality of protection setting.
- [typealias gss_iov_buffer_desc](gss_iov_buffer_desc.md)
  The structure for a vectored I/O buffer and its defined type.
- [struct gss_iov_buffer_desc_struct](gss_iov_buffer_desc_struct.md)
  The structure for a vectored I/O buffer and its defined type.
- [typealias gss_buffer_t](gss_buffer_t.md)
  A pointer to a buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [typealias gss_const_buffer_t](gss_const_buffer_t.md)
  A pointer to an immutable buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [typealias gss_buffer_set_t](gss_buffer_set_t.md)
  A pointer to the descriptor that you use to manage an array of buffer descriptors.
- [typealias gss_buffer_desc](gss_buffer_desc.md)
  The buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [struct gss_buffer_desc_struct](gss_buffer_desc_struct.md)
  The structure for a buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [typealias gss_buffer_set_desc](gss_buffer_set_desc.md)
  The descriptor that you use to manage an array of buffer descriptors.
- [struct gss_buffer_set_desc_struct](gss_buffer_set_desc_struct.md)
  The structure for a buffer set descriptor that you use to manage an array of buffer descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_iov_buffer_t)*