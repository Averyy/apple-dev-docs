# gss_set_cred_option(_:_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Changes a credential option.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_set_cred_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t?>?, _ object: gss_OID, _ value: gss_buffer_t?) -> OM_uint32
```

```c
OM_uint32 gss_set_cred_option(OM_uint32 *minor_status, gss_cred_id_t*cred_handle, gss_OID const object, gss_buffer_t const value);
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a description of other status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `cred_handle`: The credential to update.
- `object`: An object identifier that indicates the characteristic of the credential that should be changed.
- `value`: The new value for the named object.

## See Also

### Allocation and Deallocation
- [func GSSCreateCredentialFromUUID(CFUUID) -> gss_cred_id_t?](./gsscreatecredentialfromuuid%28_%29.md)
  Creates a credential from a universally unique identifier.
- [func gss_add_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_name_t?, gss_OID?, gss_cred_usage_t, OM_uint32, OM_uint32, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](./gss_add_cred%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Adds a new credential element to an existing credential.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](./gss_release_cred%28_,_%29.md)
  Releases the memory of a credential.
- [func gss_destroy_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](./gss_destroy_cred%28_,_%29.md)
  Purges a credential from memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_set_cred_option(_:_:_:_:))*