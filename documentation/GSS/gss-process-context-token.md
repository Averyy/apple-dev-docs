# gss_process_context_token(_:_:_:)

**Framework**: GSS  
**Kind**: func

Processes a token from a peer asynchronously.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_process_context_token(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ token_buffer: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

Normally, contexts exchange tokens during the initialization process, using [`gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:)`](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md) and in the initiator and [`gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:)`](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md) in the acceptor. Occasionally, a mechanism needs to send a token asynchronously, for example after a call to the [`gss_delete_sec_context(_:_:_:)`](gss_delete_sec_context(_:_:_:).md) function when you supply an output token buffer. The `gss_process_context_token` function provides a means to supply a token received from a peer to the context unexpectedly.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context that should handle the token.
- `token_buffer`: The token to process.

## See Also

- [func gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_ctx_id_t?>, gss_name_t, gss_OID?, OM_uint32, OM_uint32, gss_channel_bindings_t?, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Initiates a security context with a peer.
- [func gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_cred_id_t?, gss_buffer_t?, gss_channel_bindings_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md)
  Accepts a security context initiated by a peer.
- [func gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_delete_sec_context(_:_:_:).md)
  Deletes a security context.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_sec_context_option(_:_:_:_:).md)
  Sets an option on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_process_context_token(_:_:_:))*