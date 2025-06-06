# gss_add_cred(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Adds a new credential element to an existing credential.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_add_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_cred_handle: gss_cred_id_t?, _ desired_name: gss_name_t?, _ desired_mech: gss_OID?, _ cred_usage: gss_cred_usage_t, _ initiator_time_req: OM_uint32, _ acceptor_time_req: OM_uint32, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t?>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set?>?, _ initiator_time_rec: UnsafeMutablePointer<OM_uint32>?, _ acceptor_time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `input_cred_handle`: The credential to which the new element should be added. If the   parameter is  , the input credential is modified to include the new element. Otherwise, a new credential that combines the input credential with the new element is returned as the output credential. Specify   to create a new credential with default behavior, in which case the   cannot  be  .
- `desired_name`: The name of the entity for which the credential is to be acquired. Specify   to get a credential with a default name or use   to create a name object.
- `desired_mech`: The set of underlying security mechanisms to use with the credential. Use   to get the default set.
- `cred_usage`: A flag that indicates how the credential will be used. Specify   for context initiation,   for context acceptance, or   for both.
- `initiator_time_req`: The time in seconds that the credential should remain valid for initiating security contexts. Use   to indicate the maximum allowed duration. The value is ignored for credentials with usage set to  .
- `acceptor_time_req`: The time in seconds that the credential should remain valid for accepting security contexts. Use   to indicate the maximum allowed duration. The value is ignored for credentials with usage set to  .
- `output_cred_handle`: A pointer the function uses to return the credential. Set to   to modify the input credential in place. Release the credential’s memory with   when you are done with it.
- `actual_mechs`: A pointer the function uses to return the actual mechanisms used by the credential. Set to   to ignore this output. If you do receive a set of mechanisms, use   to release its memory when you are done with it.
- `initiator_time_rec`: A pointer the function uses to return the actual number of seconds for which the credential is valid as an initiator. Set to   to ignore this output.
- `acceptor_time_rec`: A pointer the function uses to return the actual number of seconds for which the credential is valid as an acceptor. Set to   to ignore this output.

## See Also

- [func GSSCreateCredentialFromUUID(CFUUID) -> gss_cred_id_t?](gsscreatecredentialfromuuid(_:).md)
  Creates a credential from a universally unique identifier.
- [func gss_set_cred_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_cred_option(_:_:_:_:).md)
  Changes a credential option.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_destroy_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_destroy_cred(_:_:).md)
  Purges a credential from memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_add_cred(_:_:_:_:_:_:_:_:_:_:_:))*