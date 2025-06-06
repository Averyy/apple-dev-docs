# GSSCredentialGetLifetime(_:)

**Framework**: GSS  
**Kind**: func

Returns the remaining time in seconds before the credential expires.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func GSSCredentialGetLifetime(_ cred: gss_cred_id_t) -> OM_uint32
```

#### Return Value

The time in seconds that the credential has before it expires. The time is 0 if the call fails, or [`GSS_C_INDEFINITE`](gss_c_indefinite.md) if the credential never expires.

## Parameters

- `cred`: The credential to inspect.

## See Also

- [func gss_inquire_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_cred(_:_:_:_:_:_:).md)
  Obtains information about a credential.
- [func gss_inquire_cred_by_mech(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_OID, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?) -> OM_uint32](gss_inquire_cred_by_mech(_:_:_:_:_:_:_:).md)
  Obtains per-mechanism information about a credential.
- [func gss_inquire_cred_by_oid(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_inquire_cred_by_oid(_:_:_:_:).md)
  Inquires about a particular characteristic of a credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gsscredentialgetlifetime(_:))*