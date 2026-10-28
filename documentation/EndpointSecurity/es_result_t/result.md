# result

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The message’s result, as either an authorization result or flags.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var result: es_result_t.__Unnamed_union_result
```

```c
union { ... } result;
```

## Discussion

This type is a `union` of an [`es_auth_result_t`](../es_auth_result_t.md) named `auth` and a [`uint32_t`](../../kernel/uint32_t.md) named `flags`. Use the [`result_type`](./result_type.md) field to determine which type this result represents.

## Topics

### Instance Properties
- [auth](./result/auth.md)
- [flags](./result/flags.md)
- [reserved](./result/reserved.md)

## See Also

### Inspecting Result Properties
- [var result_type: es_result_type_t](./result_type.md)
  The type of the message’s result.
- [struct es_result_type_t](../es_result_type_t.md)
  A type that indicates the type of a message’s result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_result_t/result)*