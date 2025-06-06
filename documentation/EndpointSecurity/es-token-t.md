# es_token_t

**Framework**: Endpoint Security  
**Kind**: struct

An arbitrary buffer of data with its size.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_token_t
```

## Topics

### Inspecting the Token
- [var data: UnsafePointer<UInt8>!](es_token_t/data.md)
  A data buffer.
- [var size: Int](es_token_t/size.md)
  The size of the data buffer, in bytes.
### Initializers
- [init()](es_token_t/init.md)
- [init(size: Int, data: UnsafePointer<UInt8>!)](es_token_t/init(size:data:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [struct es_string_token_t](es_string_token_t.md)
  A pointer to a null-terminated string, and the length in bytes of that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_token_t)*