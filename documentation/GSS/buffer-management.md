# Buffer Management

**Framework**: GSS  
**Role**: API Collection

Allocate and deallocate buffers with structures that hold a variety of data.

## Topics

### Buffer Data Structures
- [typealias gss_qop_t](./gss_qop_t.md)
  A quality of protection setting.
- [typealias gss_iov_buffer_t](./gss_iov_buffer_t.md)
  The structure for a vectored I/O buffer and its defined type.
- [typealias gss_iov_buffer_desc](./gss_iov_buffer_desc.md)
  The structure for a vectored I/O buffer and its defined type.
- [struct gss_iov_buffer_desc_struct](./gss_iov_buffer_desc_struct.md)
  The structure for a vectored I/O buffer and its defined type.
- [typealias gss_buffer_t](./gss_buffer_t.md)
  A pointer to a buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [typealias gss_const_buffer_t](./gss_const_buffer_t.md)
  A pointer to an immutable buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [typealias gss_buffer_set_t](./gss_buffer_set_t.md)
  A pointer to the descriptor that you use to manage an array of buffer descriptors.
- [typealias gss_buffer_desc](./gss_buffer_desc.md)
  The buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [struct gss_buffer_desc_struct](./gss_buffer_desc_struct.md)
  The structure for a buffer descriptor that you use to exchange octet streams with many GSS-API functions.
- [typealias gss_buffer_set_desc](./gss_buffer_set_desc.md)
  The descriptor that you use to manage an array of buffer descriptors.
- [struct gss_buffer_set_desc_struct](./gss_buffer_set_desc_struct.md)
  The structure for a buffer set descriptor that you use to manage an array of buffer descriptors.
- [GSS_C_NO_OID](./gss_c_no_oid.md)
  Indicates a `NULL` [`gss_OID`](./gss_oid.md) object.
- [GSS_C_NO_BUFFER](./gss_c_no_buffer.md)
  The GSS buffer object has no value.
- [GSS_C_NO_BUFFER_SET](./gss_c_no_buffer_set.md)
  The GSS buffer set object has no value.
- [GSS_C_EMPTY_BUFFER](./gss_c_empty_buffer.md)
  The GSS buffer object has no value, and its length set to zero.
- [GSS_C_NO_IOV_BUFFER](./gss_c_no_iov_buffer.md)
  The GSS IOV buffer object has no value.
### Allocation and Deallocation
- [func gss_create_empty_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](./gss_create_empty_buffer_set%28_,_%29.md)
  Allocates an empty buffer set descriptor that you use to manage an array of buffers.
- [func gss_add_buffer_set_member(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32](./gss_add_buffer_set_member%28_,_,_%29.md)
  Copies the contents of a buffer into a buffer set.
- [func gss_release_buffer(UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](./gss_release_buffer%28_,_%29.md)
  Frees the memory associated with a single buffer descriptor.
- [func gss_release_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](./gss_release_buffer_set%28_,_%29.md)
  Frees the memory associated with a buffer set descriptor and all the buffers it contains.

## See Also

### Memory and Context
- [Allocating and Releasing Objects](./allocating-and-releasing-objects.md)
  Manage memory and object lifetimes.
- [Function Status](./function-status.md)
  Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.
- [Context Services](./context-services.md)
  Use context services to manage secure operations between endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/buffer-management)*