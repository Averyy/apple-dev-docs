# gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Accepts a security context initiated by a peer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_accept_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t?>, _ acceptor_cred_handle: gss_cred_id_t?, _ input_token: gss_buffer_t?, _ input_chan_bindings: gss_channel_bindings_t?, _ src_name: UnsafeMutablePointer<gss_name_t?>?, _ mech_type: UnsafeMutablePointer<gss_OID?>?, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?, _ delegated_cred_handle: UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32
```

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: A pointer the function uses to return the context. Pass   for first call and use the value returned by the first call in continuation calls. Release the context’s resources using the    function when you are done with it.
- `acceptor_cred_handle`: The credential claimed by the acceptor. Specify   to use the default credential.
- `input_token`: The token obtained from the peer.
- `input_chan_bindings`: Channel bindings to use. Pass    if channel bindings are not used.
- `src_name`: A pointer the function uses to return the authenticated name of the context initiator. Specify   to ignore this output.
- `mech_type`: A pointer the function uses to return the mechanism used by the context. Do   free this object because it is held in static memory.  Specify   to ignore this output.
- `output_token`: A buffer the function fills with a token to transmit to the peer. If the buffer length is zero, there is no token to pass. Otherwise, free the token buffer’s memory using   when you are done with it.
- `ret_flags`: A pointer the function uses to return the flags supported by the context. See   for a list of possible values. Specify   to ignore this output.
- `time_rec`: A pointer the function uses to return the number of seconds for which the context is valid. Specify   to ignore this output.
- `delegated_cred_handle`: A pointer the function uses to return the credentials of the initiator. The function returns   unless the   parameter includes  . If the credential exists, release its memory with   when you are done with it.

## See Also

- [func gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_ctx_id_t?>, gss_name_t, gss_OID?, OM_uint32, OM_uint32, gss_channel_bindings_t?, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Initiates a security context with a peer.
- [func gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_delete_sec_context(_:_:_:).md)
  Deletes a security context.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32](gss_process_context_token(_:_:_:).md)
  Processes a token from a peer asynchronously.
- [func gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_sec_context_option(_:_:_:_:).md)
  Sets an option on a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:))*