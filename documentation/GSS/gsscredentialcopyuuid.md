# GSSCredentialCopyUUID(_:)

**Framework**: GSS  
**Kind**: func

Returns a copy of the universally unique identifier corresponding to a GSS credential.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func GSSCredentialCopyUUID(_ credential: gss_cred_id_t) -> Unmanaged<CFUUID>?
```

#### Return Value

A `CFUUID` object that corresponds to the given credential. Use `CFRelease` to free this object’s memory when you are done with it.

#### Discussion

When you want to restore the credential from the `CFUUID`, use [`GSSCreateCredentialFromUUID(_:)`](gsscreatecredentialfromuuid(_:).md).

## Parameters

- `credential`: The credential whose unique identifier you want.

## See Also

- [func gss_aapl_initial_cred(gss_name_t, gss_const_OID, CFDictionary?, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](gss_aapl_initial_cred(_:_:_:_:_:).md)
  Acquires a new credential using a password or certificate.
- [func gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t?, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred(_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context.
- [func gss_acquire_cred_with_password(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred_with_password(_:_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context using a password.
- [func GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t?](gsscredentialcopyname(_:).md)
  Returns the name describing the credential.
- [func gss_pseudo_random(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, Int, gss_buffer_t) -> OM_uint32](gss_pseudo_random(_:_:_:_:_:_:).md)
  Returns a pseudo-random byte stream for keying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gsscredentialcopyuuid(_:))*