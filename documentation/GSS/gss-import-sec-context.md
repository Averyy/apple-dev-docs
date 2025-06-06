# gss_import_sec_context(_:_:_:)

**Framework**: GSS  
**Kind**: func

Imports a security context from another process.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_import_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ interprocess_token: gss_buffer_t, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t?>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

You can import an interprocess token only once. After you have imported it, release the token’s buffer using a call to [`gss_release_buffer(_:_:)`](gss_release_buffer(_:_:).md).

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `interprocess_token`: The token created by a call to  .
- `context_handle`: A pointer the function uses to return the imported context. Release the context with the   function when you are done with it.

## See Also

- [func gss_export_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_export_sec_context(_:_:_:).md)
  Transfers a security context to another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_import_sec_context(_:_:_:))*