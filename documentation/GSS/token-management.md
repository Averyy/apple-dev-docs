# Token Management

**Framework**: GSS

Establish secure communication with tokens.

#### Overview

The basic unit of currency in the GSS-API is the token. Applications using the GSS-API communicate with each other by using tokens, both for exchanging data and for making security arrangements. Tokens are declared as [`gss_buffer_t`](gss_buffer_t.md) data types and are opaque to applications.

## Topics

### Buffer Flags
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
- [var GSS_IOV_BUFFER_TYPE_FLAG_MASK: UInt32](gss_iov_buffer_type_flag_mask.md)
  The buffer type is a flag mask.
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
### Encapsulation and Decapsulation
- [func gss_encapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32](gss_encapsulate_token(_:_:_:).md)
  Returns a buffer encapsulating the given token.
- [func gss_decapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32](gss_decapsulate_token(_:_:_:).md)
  Returns a token encapsulated in a buffer.

## See Also

- [Message Protection](message-protection.md)
  Provide cryptographic protection to secure message integrity.
- [Kerberos Implementation](kerberos-implementation.md)
  Establish secure connections using the Kerberos implementation of GSS-API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/token-management)*