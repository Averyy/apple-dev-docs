# es_result_t

**Framework**: Endpoint Security  
**Kind**: struct

The result of the Endpoint Security subsystem authorization process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_result_t
```

## Topics

### Inspecting Result Properties
- [var result: es_result_t.__Unnamed_union_result](es_result_t/result.md)
  The message’s result, as either an authorization result or flags.
- [var result_type: es_result_type_t](es_result_t/result_type.md)
  The type of the message’s result.
- [struct es_result_type_t](es_result_type_t.md)
  A type that indicates the type of a message’s result.
### Initializers
- [init()](es_result_t/init.md)
- [init(result_type: es_result_type_t, result: es_result_t.__Unnamed_union_result)](es_result_t/init(result_type:result:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_string_token_t](es_string_token_t.md)
  A pointer to a null-terminated string, and the length in bytes of that string.
- [struct es_token_t](es_token_t.md)
  An arbitrary buffer of data with its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_result_t)*