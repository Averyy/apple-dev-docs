# Message Protection

**Framework**: GSS

Provide cryptographic protection to secure message integrity.

## Topics

### Message Wrapping and Verification
- [func gss_get_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_qop_t, gss_buffer_t, gss_buffer_t) -> OM_uint32](gss_get_mic(_:_:_:_:_:).md)
  Returns a token that contains the MIC for a message.
- [func gss_verify_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](gss_verify_mic(_:_:_:_:_:).md)
  Returns an indication of whether the integrity of a message is intact, given its MIC token.
- [func gss_wrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, gss_buffer_t, UnsafeMutablePointer<Int32>?, gss_buffer_t) -> OM_uint32](gss_wrap(_:_:_:_:_:_:_:).md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.
- [func gss_unwrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](gss_unwrap(_:_:_:_:_:_:).md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.
- [func gss_sign(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, gss_buffer_t) -> OM_uint32](gss_sign(_:_:_:_:_:).md)
  Returns a digital signature for a message.
- [func gss_verify(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_verify(_:_:_:_:_:).md)
  Returns a flag that indicates the integrity of a message’s digital signature.
- [func gss_seal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, Int32, gss_buffer_t, UnsafeMutablePointer<Int32>, gss_buffer_t) -> OM_uint32](gss_seal(_:_:_:_:_:_:_:).md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.
- [func gss_unseal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_unseal(_:_:_:_:_:_:).md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.

## See Also

- [Token Management](token-management.md)
  Establish secure communication with tokens.
- [Kerberos Implementation](kerberos-implementation.md)
  Establish secure connections using the Kerberos implementation of GSS-API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/message-protection)*