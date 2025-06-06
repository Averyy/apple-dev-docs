# gss_export_sec_context(_:_:_:)

**Framework**: GSS  
**Kind**: func

Transfers a security context to another process.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_export_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t?>, _ interprocess_token: gss_buffer_t?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

The function deactivates the context before exporting it. Use [`gss_import_sec_context(_:_:_:)`](gss_import_sec_context(_:_:_:).md) to restore the token to a context and reactivate it. Only one instance of a given context may be active at a time.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `context_handle`: The context to export.
- `interprocess_token`: A buffer the function fills with a token corresponding to the context. Release the buffer storage with a call to   when you are done with it.

## See Also

- [func gss_import_sec_context(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_ctx_id_t?>) -> OM_uint32](gss_import_sec_context(_:_:_:).md)
  Imports a security context from another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_export_sec_context(_:_:_:))*