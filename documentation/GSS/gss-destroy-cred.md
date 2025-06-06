# gss_destroy_cred(_:_:)

**Framework**: GSS  
**Kind**: func

Purges a credential from memory.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_destroy_cred(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32
```

## Mentions

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

This function actively purges the credential from memory and then calls [`gss_release_cred(_:_:)`](gss_release_cred(_:_:).md) to free the memory. This is a more secure option than calling the release function directly.

## Parameters

- `min_stat`: A pointer to the secondary status result that provides additional information in case of failure.
- `cred_handle`: The credential to eliminate from memory.

## See Also

- [func GSSCreateCredentialFromUUID(CFUUID) -> gss_cred_id_t?](gsscreatecredentialfromuuid(_:).md)
  Creates a credential from a universally unique identifier.
- [func gss_add_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_name_t?, gss_OID?, gss_cred_usage_t, OM_uint32, OM_uint32, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_add_cred(_:_:_:_:_:_:_:_:_:_:_:).md)
  Adds a new credential element to an existing credential.
- [func gss_set_cred_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_cred_option(_:_:_:_:).md)
  Changes a credential option.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_destroy_cred(_:_:))*