# gss_seal(_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Returns a secure message created by calculating and attaching a MIC to the input message, and then optionally encrypting it.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`gss_wrap(_:_:_:_:_:_:_:)`](./gss_wrap%28_,_,_,_,_,_,_%29.md) instead.

## Declaration

```swift
func gss_seal(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: Int32, _ input_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>, _ output_message_buffer: gss_buffer_t) -> OM_uint32
```

```c
OM_uint32 gss_seal(OM_uint32 *minor_status, gss_ctx_id_t context_handle, int conf_req_flag, int qop_req, gss_buffer_t input_message_buffer, int *conf_state, gss_buffer_t output_message_buffer);
```

## Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context used to send the message.
- `conf_req_flag`: A flag you set to zero to request that only that the message integrity check be applied, or to anything non-zero to request both integrity checking and confidentiality (encryption) of the message.
- `qop_req`: The quality of protection requested for the encryption. See `Quality of Protection Settings` for valid values.
- `input_message_buffer`: A buffer containing the message to protect.
- `conf_state`: A pointer the function uses to indicate what protection is actually applied to the message. A value of zero indicates only integrity checking. A non-zero value indicates both integrity checking and confidentiality. Pass `NULL` to ignore this output.
- `output_message_buffer`: A buffer the function fills with the fully wrapped message, ready for transport to the peer. Release the buffer using a call to [`gss_release_buffer(_:_:)`](./gss_release_buffer%28_,_%29.md) when you are done with it.

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
- [func gss_unseal(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> OM_uint32](./gss_unseal%28_,_,_,_,_,_%29.md)
  Returns the original version of a secure message by optionally decrypting it and then extracting and verifying the attached MIC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_seal(_:_:_:_:_:_:_:))*