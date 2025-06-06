# gss_export_cred(_:_:_:)

**Framework**: GSS  
**Kind**: func

Exports a credential to a token.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_export_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ token: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

You can recover the credential exported this way using [`gss_import_cred(_:_:_:)`](gss_import_cred(_:_:_:).md).

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `cred_handle`: The credential that you want to export.
- `token`: A buffer representing a token that the function fills with data that represents the credential. Anything in the buffer from before the call, is discarded, even if export fails.

## See Also

- [func gss_import_cred(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_import_cred(_:_:_:).md)
  Imports a credential from a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_export_cred(_:_:_:))*