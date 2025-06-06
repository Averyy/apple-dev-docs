# gss_verify_mic(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns an indication of whether the integrity of a message is intact, given its MIC token.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_verify_mic(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ message_buffer: gss_buffer_t, _ token_buffer: gss_buffer_t, _ qop_state: UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) if the message is valid, or another value that indicates the reason for failure. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context used to send the message.
- `message_buffer`: A buffer holding the message to verify.
- `token_buffer`: A buffer holding the token representing the cryptographic signature the protects the message.
- `qop_state`: A pointer the function uses to return the quality of protection setting. See Quality of Protection Constants in   for valid values. Pass   to ignore this output.

## See Also

- [func gss_get_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_qop_t, gss_buffer_t, gss_buffer_t) -> OM_uint32](gss_get_mic(_:_:_:_:_:).md)
  Returns a token that contains the MIC for a message.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_verify_mic(_:_:_:_:_:))*