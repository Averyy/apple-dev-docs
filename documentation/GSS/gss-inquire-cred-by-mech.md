# gss_inquire_cred_by_mech(_:_:_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Obtains per-mechanism information about a credential.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_inquire_cred_by_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t?, _ mech_type: gss_OID, _ cred_name: UnsafeMutablePointer<gss_name_t?>?, _ initiator_lifetime: UnsafeMutablePointer<OM_uint32>?, _ acceptor_lifetime: UnsafeMutablePointer<OM_uint32>?, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `cred_handle`: The credential to inspect. Use   to inquire about the default initiator principal.
- `mech_type`: The mechanism for which information should be returned.
- `cred_name`: A pointer the function uses to return the name that the credential asserts. Use   to free the name  object’s memory when you are done with it. Set the parameter to   to ignore this output.
- `initiator_lifetime`: A pointer the function uses to return the number of seconds for which the credential will remain valid for initiating security contexts, or 0 if the credential is expired or if the credential’s usage mechanism is  . For credentials that do not support expiry, the function returns  . Set to   to ignore this output.
- `acceptor_lifetime`: A pointer the function uses to return the number of seconds for which the credential will remain valid for accepting security contexts, or 0 if the credential is expired or if the credential’s usage mechanism is  . For credentials that do not support expiry, the function returns  . Set to   to ignore this output.
- `cred_usage`: A pointer the function uses to return the credential usage. The value is one of  ,  , or  . Set to   to ignore this output.

## See Also

- [func gss_inquire_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_cred(_:_:_:_:_:_:).md)
  Obtains information about a credential.
- [func gss_inquire_cred_by_oid(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_inquire_cred_by_oid(_:_:_:_:).md)
  Inquires about a particular characteristic of a credential.
- [func GSSCredentialGetLifetime(gss_cred_id_t) -> OM_uint32](gsscredentialgetlifetime(_:).md)
  Returns the remaining time in seconds before the credential expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_inquire_cred_by_mech(_:_:_:_:_:_:_:))*