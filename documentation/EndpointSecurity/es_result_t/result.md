# result

**Framework**: Endpoint Security  
**Kind**: property

The message’s result, as either an authorization result or flags.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var result: es_result_t.__Unnamed_union_result
```

#### Discussion

This type is a `union` of an [`es_auth_result_t`](es_auth_result_t.md) named `auth` and a [`uint32_t`](https://developer.apple.com/documentation/kernel/uint32_t) named `flags`. Use the [`result_type`](es_result_t/result_type.md) field to determine which type this result represents.

## See Also

- [var result_type: es_result_type_t](es_result_t/result_type.md)
  The type of the message’s result.
- [struct es_result_type_t](es_result_type_t.md)
  A type that indicates the type of a message’s result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_result_t/result)*