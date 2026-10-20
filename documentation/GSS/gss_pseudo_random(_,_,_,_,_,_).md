# gss_pseudo_random(_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Returns a pseudo-random byte stream for keying.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_pseudo_random(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context: gss_ctx_id_t, _ prf_key: Int32, _ prf_in: gss_buffer_t, _ desired_output_len: Int, _ prf_out: gss_buffer_t) -> OM_uint32
```

```c
OM_uint32 gss_pseudo_random(OM_uint32 *minor_status, gss_ctx_id_t context, int prf_key, gss_buffer_t const prf_in, ssize_t desired_output_len, gss_buffer_t prf_out);
```

## See Also

### Acquisition
- [func gss_aapl_initial_cred(gss_name_t, gss_const_OID, CFDictionary?, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](./gss_aapl_initial_cred%28_,_,_,_,_%29.md)
  Acquires a new credential using a password or certificate.
- [func gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t?, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](./gss_acquire_cred%28_,_,_,_,_,_,_,_%29.md)
  Acquires a credential for use in establishing a security context.
- [func gss_acquire_cred_with_password(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](./gss_acquire_cred_with_password%28_,_,_,_,_,_,_,_,_%29.md)
  Acquires a credential for use in establishing a security context using a password.
- [func GSSCredentialCopyUUID(gss_cred_id_t) -> Unmanaged<CFUUID>?](./gsscredentialcopyuuid%28_%29.md)
  Returns a copy of the universally unique identifier corresponding to a GSS credential.
- [func GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t?](./gsscredentialcopyname%28_%29.md)
  Returns the name describing the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_pseudo_random(_:_:_:_:_:_:))*