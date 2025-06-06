# gss_inquire_cred_by_oid(_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Inquires about a particular characteristic of a credential.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_inquire_cred_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `cred_handle`: The credential to inquire about.
- `desired_object`: The object identifier of the characteristic of the credential to return.
- `data_set`: A pointer the function uses to return a set of buffers that contain the results across all of the credential’s mechanisms. If the desired object is not found, this is set to  . Otherwise, call   to free the memory of this object when you are done with it.

## See Also

- [func gss_inquire_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_cred(_:_:_:_:_:_:).md)
  Obtains information about a credential.
- [func gss_inquire_cred_by_mech(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_OID, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?) -> OM_uint32](gss_inquire_cred_by_mech(_:_:_:_:_:_:_:).md)
  Obtains per-mechanism information about a credential.
- [func GSSCredentialGetLifetime(gss_cred_id_t) -> OM_uint32](gsscredentialgetlifetime(_:).md)
  Returns the remaining time in seconds before the credential expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_inquire_cred_by_oid(_:_:_:_:))*