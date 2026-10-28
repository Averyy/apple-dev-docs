# gss_verify(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Returns a flag that indicates the integrity of a message’s digital signature.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`gss_verify_mic(_:_:_:_:_:)`](./gss_verify_mic%28_,_,_,_,_%29.md) instead.

## Declaration

```swift
func gss_verify(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ message_buffer: gss_buffer_t, _ token_buffer: gss_buffer_t, _ qop_state: UnsafeMutablePointer<Int32>) -> OM_uint32
```

```c
OM_uint32 gss_verify(OM_uint32 *minor_status, gss_ctx_id_t context_handle, gss_buffer_t message_buffer, gss_buffer_t token_buffer, int *qop_state);
```

## Return Value

A status code set to GSS_S_COMPLETE on success. See Status Codes for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context used to send the message.
- `message_buffer`: A buffer holding the message to verify.
- `token_buffer`: A buffer holding the token representing the cryptographic signature the protects the message.
- `qop_state`: A pointer the function uses to return the quality of protection setting. See Quality of Protection Constants in [Object Identifiers](./object-identifiers.md) for valid values. Pass NULL to ignore this output.

## See Also

### Message Wrapping and Verification
- [func gss_get_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_qop_t, gss_buffer_t, gss_buffer_t) -> OM_uint32](./gss_get_mic%28_,_,_,_,_%29.md)
  Returns a token that contains the MIC for a message.
- [func gss_verify_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](./gss_verify_mic%28_,_,_,_,_%29.md)
  Returns an indication of whether the integrity of a message is intact, given its MIC token.
- [func gss_wrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, gss_buffer_t, UnsafeMutablePointer<Int32>?, gss_buffer_t) -> OM_uint32](./gss_wrap%28_,_,_,_,_,_,_%29.md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.
- [func gss_unwrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](./gss_unwrap%28_,_,_,_,_,_%29.md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.
- [func gss_sign(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, gss_buffer_t) -> OM_uint32](./gss_sign%28_,_,_,_,_%29.md)
  Returns a digital signature for a message.
- [func gss_seal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, Int32, gss_buffer_t, UnsafeMutablePointer<Int32>, gss_buffer_t) -> OM_uint32](./gss_seal%28_,_,_,_,_,_,_%29.md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.
- [func gss_unseal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> OM_uint32](./gss_unseal%28_,_,_,_,_,_%29.md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_verify(_:_:_:_:_:))*