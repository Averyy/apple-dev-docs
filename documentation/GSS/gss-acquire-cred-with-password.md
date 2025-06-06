# gss_acquire_cred_with_password(_:_:_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Acquires a credential for use in establishing a security context using a password.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_acquire_cred_with_password(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t, _ password: gss_buffer_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set?, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t?>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set?>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `desired_name`: The name of the principal whose credential should be acquired. Specify   to get a generic credential or use   to obtain a name object.
- `password`: The password.
- `time_req`: The time in seconds that the credential should remain valid. Use   to indicate the maximum allowed duration.
- `desired_mechs`: The set of underlying security mechanisms to use with the credential. Use   to get the default set.
- `cred_usage`: A flag that indicates how the credential will be used. Specify   for context initiation,   for context acceptance, or   for both.
- `output_cred_handle`: A pointer the function uses to return the credential. Release the credential’s memory with   when you are done with it.
- `actual_mechs`: A pointer the function uses to return the actual mechanisms used by the credential. Set to   to ignore this output. If you do receive a set of mechanisms, use   to release its memory when you are done with it.
- `time_rec`: A pointer the function uses to return the actual number of seconds for which the credential is valid. Set to   to ignore this output.

## See Also

- [func gss_aapl_initial_cred(gss_name_t, gss_const_OID, CFDictionary?, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](gss_aapl_initial_cred(_:_:_:_:_:).md)
  Acquires a new credential using a password or certificate.
- [func gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t?, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred(_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context.
- [func GSSCredentialCopyUUID(gss_cred_id_t) -> Unmanaged<CFUUID>?](gsscredentialcopyuuid(_:).md)
  Returns a copy of the universally unique identifier corresponding to a GSS credential.
- [func GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t?](gsscredentialcopyname(_:).md)
  Returns the name describing the credential.
- [func gss_pseudo_random(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, Int, gss_buffer_t) -> OM_uint32](gss_pseudo_random(_:_:_:_:_:_:).md)
  Returns a pseudo-random byte stream for keying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_acquire_cred_with_password(_:_:_:_:_:_:_:_:_:))*