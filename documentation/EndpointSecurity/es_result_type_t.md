# es_result_type_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

A type that indicates the type of a message’s result.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_result_type_t
```

```c
typedef enum { ... } es_result_type_t;
```

## Topics

### Result Types
- [var ES_RESULT_TYPE_AUTH: es_result_type_t](./es_result_type_auth.md)
  The authorization result type.
- [var ES_RESULT_TYPE_FLAGS: es_result_type_t](./es_result_type_flags.md)
  The flags result type.
### Initializers
- [init(UInt32)](./es_result_type_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_result_type_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_result_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Inspecting Result Properties
- [var result: es_result_t.__Unnamed_union_result](./es_result_t/result.md)
  The message’s result, as either an authorization result or flags.
- [var result_type: es_result_type_t](./es_result_t/result_type.md)
  The type of the message’s result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_result_type_t)*