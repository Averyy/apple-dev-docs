# result_type

**Framework**: Endpoint Security  
**Kind**: property

The type of the message’s result.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var result_type: es_result_type_t
```

#### Discussion

Use this value to determine which member of the [`result`](es_result_t/result.md) `union` to use: `auth` or `flags`.

## See Also

- [var result: es_result_t.__Unnamed_union_result](es_result_t/result.md)
  The message’s result, as either an authorization result or flags.
- [struct es_result_type_t](es_result_type_t.md)
  A type that indicates the type of a message’s result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_result_t/result_type)*