# gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Initiates a security context with a peer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_init_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ initiator_cred_handle: gss_cred_id_t?, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t?>, _ target_name: gss_name_t, _ input_mech_type: gss_OID?, _ req_flags: OM_uint32, _ time_req: OM_uint32, _ input_chan_bindings: gss_channel_bindings_t?, _ input_token: gss_buffer_t?, _ actual_mech_type: UnsafeMutablePointer<gss_OID?>?, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32
```

#### Return Value

A status code indicating the outcome of the call. A code of [`GSS_S_COMPLETE`](gss_s_complete.md) means the context is complete. A code of [`GSS_S_CONTINUE_NEEDED`](gss_s_continue_needed.md) indicates the need for another round of calls. Any other return code represents an error condition. See [`Function Status`](function-status.md) for a complete list of possible status results.

#### Discussion

Don’t call this function on a UI update thread because it may block on network activity.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `initiator_cred_handle`: The credential to use when building the context. Pass   to use the default credential for the mechanism.
- `context_handle`: A pointer the function uses to return the context. Pass   for first call and use the value returned by the first call in continuation calls. Release the context’s resources using the    function when you are done with it.
- `target_name`: The name of the target acceptor, created with  . The name must be of a type that is supported by the mechanism, as given by  .
- `input_mech_type`: The mechanism type to use. Pass   to try Kerberos ( ) as a default.
- `req_flags`: Logical OR of the flags to use when building the context. See   for a list of possible values.
- `time_req`: The time in seconds that the context should be valid. Use   to request the longest available time.
- `input_chan_bindings`: Channel bindings to use. Pass   if channel bindings are not used.
- `input_token`: A token sent from the acceptor. On the first call, use  .
- `actual_mech_type`: A pointer the function uses to return the actual mechanism used by the context. Do   free this object because it is held in static memory.
- `output_token`: A buffer the function fills with an opaque token that you send to the acceptor. If the length of the buffer is non-zero, a token exists and you send it to the acceptor no matter the return status, whether complete, continue, or any error condition.
- `ret_flags`: A pointer the function uses to return the actual flags supported by the context. See   for a list of possible values.
- `time_rec`: A pointer the function uses to return the actual number of seconds for which the context is valid. Pass   to ignore this output.

## See Also

- [func gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_cred_id_t?, gss_buffer_t?, gss_channel_bindings_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md)
  Accepts a security context initiated by a peer.
- [func gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_delete_sec_context(_:_:_:).md)
  Deletes a security context.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32](gss_process_context_token(_:_:_:).md)
  Processes a token from a peer asynchronously.
- [func gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_sec_context_option(_:_:_:_:).md)
  Sets an option on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:))*