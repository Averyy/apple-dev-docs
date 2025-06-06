# gss_decapsulate_token(_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a token encapsulated in a buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_decapsulate_token(_ input_token: gss_const_buffer_t, _ oid: gss_const_OID, _ output_token: gss_buffer_t) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

#### Discussion

Use this function to reverse the encapsulation provided by [`gss_encapsulate_token(_:_:_:)`](gss_encapsulate_token(_:_:_:).md).

## Parameters

- `input_token`: A buffer holding the encapsulated token.
- `oid`: The expected object identifier of the token.
- `output_token`: A buffer the function fills with the decapsulated token data. Release this buffer’s memory with a call to   when you are done with it.

## See Also

- [func gss_encapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32](gss_encapsulate_token(_:_:_:).md)
  Returns a buffer encapsulating the given token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_decapsulate_token(_:_:_:))*