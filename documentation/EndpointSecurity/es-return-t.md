# es_return_t

**Framework**: Endpoint Security  
**Kind**: struct

Values that indicate the result of an Endpoint Security action that can only succeed or fail.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_return_t
```

## Topics

### Return Values
- [var ES_RETURN_SUCCESS: es_return_t](es_return_success.md)
  The action succeeded.
- [var ES_RETURN_ERROR: es_return_t](es_return_error.md)
  The action failed with an error.
### Initializers
- [init(UInt32)](es_return_t/init(_:).md)
- [init(rawValue: UInt32)](es_return_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_return_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_return_t)*