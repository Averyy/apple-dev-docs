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
- `input_cred_handle`: The credential to which the new element should be added. If the `output_cred_handle` parameter is `NULL`, the input credential is modified to include the new element. Otherwise, a new credential that combines the input credential with the new element is returned as the output credential. Specify [`GSS_C_NO_CREDENTIAL`](gss_c_no_credential.md) to create a new credential with default behavior, in which case the `output_cred_handle` cannot  be `NULL`.
- `desired_name`: The name of the entity for which the credential is to be acquired. Specify [`GSS_C_NO_NAME`](gss_c_no_name.md) to get a credential with a default name or use [`gss_import_name(_:_:_:_:)`](gss_import_name(_:_:_:_:).md) to create a name object.
- `desired_mech`: The set of underlying security mechanisms to use with the credential. Use `GSS_C_NO_OID_SET` to get the default set.
- `cred_usage`: A flag that indicates how the credential will be used. Specify [`GSS_C_INITIATE`](gss_c_initiate.md) for context initiation, [`GSS_C_ACCEPT`](gss_c_accept.md) for context acceptance, or [`GSS_C_BOTH`](gss_c_both.md) for both.
- `initiator_time_req`: The time in seconds that the credential should remain valid for initiating security contexts. Use [`GSS_C_INDEFINITE`](gss_c_indefinite.md) to indicate the maximum allowed duration. The value is ignored for credentials with usage set to [`GSS_C_ACCEPT`](gss_c_accept.md).
- `acceptor_time_req`: The time in seconds that the credential should remain valid for accepting security contexts. Use [`GSS_C_INDEFINITE`](gss_c_indefinite.md) to indicate the maximum allowed duration. The value is ignored for credentials with usage set to [`GSS_C_INITIATE`](gss_c_initiate.md).
- `output_cred_handle`: A pointer the function uses to return the credential. Set to `NULL` to modify the input credential in place. Release the credential’s memory with [`gss_release_cred(_:_:)`](gss_release_cred(_:_:).md) when you are done with it.
- `actual_mechs`: A pointer the function uses to return the actual mechanisms used by the credential. Set to `NULL` to ignore this output. If you do receive a set of mechanisms, use [`gss_release_oid_set(_:_:)`](gss_release_oid_set(_:_:).md) to release its memory when you are done with it.
- `initiator_time_rec`: A pointer the function uses to return the actual number of seconds for which the credential is valid as an initiator. Set to `NULL` to ignore this output.
- `acceptor_time_rec`: A pointer the function uses to return the actual number of seconds for which the credential is valid as an acceptor. Set to `NULL` to ignore this output.

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