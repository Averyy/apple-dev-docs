# gss_export_name(_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a mechanism name in contiguous octet format.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_export_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ exported_name: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `input_name`: The mechanism name to export. You typically obtain a name in this format from either the   or the   function.
- `exported_name`: A buffer the function fills with a contiguous octet format version of the name. Release the buffer with a call to   when you are done with it.

## See Also

- [func gss_import_name(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, gss_const_OID?, UnsafeMutablePointer<gss_name_t?>) -> OM_uint32](gss_import_name(_:_:_:_:).md)
  Converts a name in contiguous octet format to the internal name format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_export_name(_:_:_:))*