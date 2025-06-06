# es_string_token_t

**Framework**: Endpoint Security  
**Kind**: struct

A pointer to a null-terminated string, and the length in bytes of that string.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_string_token_t
```

#### Overview

The length doesn’t include the null terminator character.

## Topics

### Initializers
- [init()](es_string_token_t/init.md)
- [init(length: Int, data: UnsafePointer<CChar>!)](es_string_token_t/init(length:data:).md)
### Inspecting the Token
- [var data: UnsafePointer<CChar>!](es_string_token_t/data.md)
  The string data.
- [var length: Int](es_string_token_t/length.md)
  The size of the data buffer, in bytes.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [struct es_token_t](es_token_t.md)
  An arbitrary buffer of data with its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_string_token_t)*