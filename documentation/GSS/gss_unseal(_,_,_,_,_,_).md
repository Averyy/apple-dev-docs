# gss_unseal(_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`gss_unwrap(_:_:_:_:_:_:)`](./gss_unwrap%28_,_,_,_,_,_%29.md) instead.

## Declaration

```swift
func gss_unseal(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ input_message_buffer: gss_buffer_t, _ output_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>, _ qop_state: UnsafeMutablePointer<Int32>) -> OM_uint32
```

```c
OM_uint32 gss_unseal(OM_uint32 *minor_status, gss_ctx_id_t context_handle, gss_buffer_t input_message_buffer, gss_buffer_t output_message_buffer, int *conf_state, int *qop_state);
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context used to send the message.
- `input_message_buffer`: A buffer containing the protected message from the peer.
- `output_message_buffer`: A buffer the function uses to return the unwrapped message. Release the buffer using a call to [`gss_release_buffer(_:_:)`](./gss_release_buffer%28_,_%29.md) when you are done with it.
- `conf_state`: A pointer the function uses to indicate what protection had been applied to the message. A value of zero indicates only integrity checking. A non-zero value indicates both integrity checking and confidentiality. Pass `NULL` to ignore this output.
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
- [func gss_verify(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>) -> OM_uint32](./gss_verify%28_,_,_,_,_%29.md)
  Returns a flag that indicates the integrity of a message’s digital signature.
- [func gss_seal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, Int32, gss_buffer_t, UnsafeMutablePointer<Int32>, gss_buffer_t) -> OM_uint32](./gss_seal%28_,_,_,_,_,_,_%29.md)
  Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_unseal(_:_:_:_:_:_:))*