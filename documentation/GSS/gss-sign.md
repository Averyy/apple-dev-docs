# gss_sign(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a digital signature for a message.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func gss_sign(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ qop_req: Int32, _ message_buffer: gss_buffer_t, _ message_token: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context used to send the message.
- `qop_req`: The quality of protection requested for the message. See Quality of Protection Constants for valid values.
- `message_buffer`: A buffer holding the message to be protected.
- `message_token`: A buffer the function fills with the protection token. Release this buffer with a call to   when you are done with it.

## See Also

- [func gss_get_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_qop_t, gss_buffer_t, gss_buffer_t) -> OM_uint32](gss_get_mic(_:_:_:_:_:).md)
  Returns a token that contains the MIC for a message.
- [func gss_verify_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](gss_verify_mic(_:_:_:_:_:).md)
  Returns an indication of whether the integrity of a message is intact, given its MIC token.
- [func gss_wrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, gss_buffer_t, UnsafeMutablePointer<Int32>?, gss_buffer_t) -> OM_uint32](gss_wrap(_:_:_:_:_:_:_:).md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.
- [func gss_unwrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](gss_unwrap(_:_:_:_:_:_:).md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.
- [func gss_verify(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_verify(_:_:_:_:_:).md)
  Returns a flag that indicates the integrity of a message’s digital signature.
- [func gss_seal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, Int32, gss_buffer_t, UnsafeMutablePointer<Int32>, gss_buffer_t) -> OM_uint32](gss_seal(_:_:_:_:_:_:_:).md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.
- [func gss_unseal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_unseal(_:_:_:_:_:_:).md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_sign(_:_:_:_:_:))*