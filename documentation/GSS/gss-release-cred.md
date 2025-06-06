# gss_release_cred(_:_:)

**Framework**: GSS  
**Kind**: func

Releases the memory of a credential.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_release_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32
```

## Mentions

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

This function frees the memory associated with the credential, but doesn’t necessarily purge that memory of the credential’s data. If you need to ensure no trace of the credential remains in memory, use [`gss_destroy_cred(_:_:)`](gss_destroy_cred(_:_:).md) instead. That function first removes the credential data from memory and then frees the memory using a call to this function.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `cred_handle`: The credential whose memory should be freed.

## See Also

- [func gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_ctx_id_t?>, gss_name_t, gss_OID?, OM_uint32, OM_uint32, gss_channel_bindings_t?, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Initiates a security context with a peer.
- [func gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_cred_id_t?, gss_buffer_t?, gss_channel_bindings_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md)
  Accepts a security context initiated by a peer.
- [func gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_delete_sec_context(_:_:_:).md)
  Deletes a security context.
- [func gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32](gss_process_context_token(_:_:_:).md)
  Processes a token from a peer asynchronously.
- [func gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_sec_context_option(_:_:_:_:).md)
  Sets an option on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_release_cred(_:_:))*