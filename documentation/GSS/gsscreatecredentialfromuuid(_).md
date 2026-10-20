# GSSCreateCredentialFromUUID(_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Creates a credential from a universally unique identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func GSSCreateCredentialFromUUID(_ uuid: CFUUID) -> gss_cred_id_t?
```

```c
gss_cred_id_tGSSCreateCredentialFromUUID(CFUUIDRef uuid);
```

#### Return Value

A GSS credential for a given `CF``UUID` object if the credential exists, otherwise `NULL`. Free the credential’s memory with [`gss_release_cred(_:_:)`](./gss_release_cred%28_,_%29.md) when you are done with it.

#### Discussion

Use this function to get the credential corresponding to a `CFUUID` object that you originally obtained using a call to [`GSSCredentialCopyUUID(_:)`](./gsscredentialcopyuuid%28_%29.md).

## Parameters

- `uuid`: The universally unique identifier of the credential to fetch.

## See Also

### Allocation and Deallocation
- [func gss_add_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_name_t?, gss_OID?, gss_cred_usage_t, OM_uint32, OM_uint32, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](./gss_add_cred%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Adds a new credential element to an existing credential.
- [func gss_set_cred_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>?, gss_OID, gss_buffer_t?) -> OM_uint32](./gss_set_cred_option%28_,_,_,_%29.md)
  Changes a credential option.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](./gss_release_cred%28_,_%29.md)
  Releases the memory of a credential.
- [func gss_destroy_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](./gss_destroy_cred%28_,_%29.md)
  Purges a credential from memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gsscreatecredentialfromuuid(_:))*