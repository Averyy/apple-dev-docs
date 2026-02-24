# gss_aapl_initial_cred(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Acquires a new credential using a password or certificate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary?, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) if the call succeeds, or some other value indicating the reason for failure if not.

#### Discussion

Don’t call this function on a UI update thread because it may block on network activity.

## Parameters

- `desired_name`: The name to use to acquire the credential. Import the name using [`gss_import_name(_:_:_:_:)`](gss_import_name(_:_:_:_:).md). Ensure that the mechanism specified by the `desired_mech` parameter supports the name type.
- `desired_mech`: The mechanism to use to acquire the credential, for example [`GSS_KRB5_MECHANISM`](gss_krb5_mechanism.md) or [`GSS_NTLM_MECHANISM`](gss_ntlm_mechanism.md). Use [`gss_indicate_mechs(_:_:)`](gss_indicate_mechs(_:_:).md) to get a complete list of supported mechanisms.
- `attributes`: A dictionary that includes either the key [`kGSSICPassword`](kgssicpassword.md) to specify a password or [`kGSSICCertificate`](kgssiccertificate.md) to name a certificate for use in acquiring the credential. It may also contain any of the other keys listed in Initial Credential Keys in [`Credential Management`](credential-management.md) to optionally condition the operation.
- `output_cred_handle`: A credential pointer that the function sets to point at the new credential on success, or sets to [`GSS_C_NO_CREDENTIAL`](gss_c_no_credential.md) on failure. Use [`gss_release_cred(_:_:)`](gss_release_cred(_:_:).md) or [`gss_destroy_cred(_:_:)`](gss_destroy_cred(_:_:).md) to release the credential’s memory when you are done with it.
- `error`: An error pointer that the function sets to point at a new error object if the function call fails. Pass `NULL` to ignore this error. When an error does exist, it describes the reason for the failure, and you are responsible for releasing it with `CFRelease`.

## See Also

- [func gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t?, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred(_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context.
- [func gss_acquire_cred_with_password(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred_with_password(_:_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context using a password.
- [func GSSCredentialCopyUUID(gss_cred_id_t) -> Unmanaged<CFUUID>?](gsscredentialcopyuuid(_:).md)
  Returns a copy of the universally unique identifier corresponding to a GSS credential.
- [func GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t?](gsscredentialcopyname(_:).md)
  Returns the name describing the credential.
- [func gss_pseudo_random(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, Int, gss_buffer_t) -> OM_uint32](gss_pseudo_random(_:_:_:_:_:_:).md)
  Returns a pseudo-random byte stream for keying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_aapl_initial_cred(_:_:_:_:_:))*