# gss_delete_sec_context(_:_:_:)

**Framework**: GSS  
**Kind**: func

Deletes a security context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_delete_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t?>, _ output_token: gss_buffer_t?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on completion, or [`GSS_S_NO_CONTEXT`](gss_s_no_context.md) if no context was supplied.

#### Discussion

This function purges the context and all of its resources from memory, and frees all of its memory.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context to be deleted.
- `output_token`: A buffer that the function may fill with a token to send to the peer application. Typically, you pass  , indicating that no token is desired, and simply call upon the deletion function to operate locally on both sides of the connection. If a token is created, pass it to the remote peer, and free its memory with a call to  .

## See Also

- [func gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_ctx_id_t?>, gss_name_t, gss_OID?, OM_uint32, OM_uint32, gss_channel_bindings_t?, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Initiates a security context with a peer.
- [func gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_cred_id_t?, gss_buffer_t?, gss_channel_bindings_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md)
  Accepts a security context initiated by a peer.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32](gss_process_context_token(_:_:_:).md)
  Processes a token from a peer asynchronously.
- [func gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_sec_context_option(_:_:_:_:).md)
  Sets an option on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_delete_sec_context(_:_:_:))*