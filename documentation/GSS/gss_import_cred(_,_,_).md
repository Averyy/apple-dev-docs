# gss_import_cred(_:_:_:)

**Framework**: GSS  
**Kind**: func  
**Role**: Function

Imports a credential from a token.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_import_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ token: gss_buffer_t, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32
```

```c
OM_uint32 gss_import_cred(OM_uint32 *minor_status, gss_buffer_t token, gss_cred_id_t*cred_handle);
```

## Return Value

A status code set to [`GSS_S_COMPLETE`](./gss_s_complete.md) on success. See [Function Status](./function-status.md) for a description of other status outputs.

## Discussion

You can import a credential from a token created with [`gss_export_cred(_:_:_:)`](./gss_export_cred%28_,_,_%29.md).

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `token`: The token containing the data that represents the credential.
- `cred_handle`: A pointer to a credential that the function uses to return the credential. Free the credential’s memory with [`gss_release_cred(_:_:)`](./gss_release_cred%28_,_%29.md) when you are done with it.

## See Also

### Import and Export
- [func gss_export_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_buffer_t) -> OM_uint32](./gss_export_cred%28_,_,_%29.md)
  Exports a credential to a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_import_cred(_:_:_:))*