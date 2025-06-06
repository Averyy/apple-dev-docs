# es_new_client_result_t

**Framework**: Endpoint Security  
**Kind**: struct

The result of an attempt to create a new client.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_new_client_result_t
```

## Topics

### Success
- [var ES_NEW_CLIENT_RESULT_SUCCESS: es_new_client_result_t](es_new_client_result_success.md)
  Endpoint Security successfully created the new client.
### Errors
- [var ES_NEW_CLIENT_RESULT_ERR_INTERNAL: es_new_client_result_t](es_new_client_result_err_internal.md)
  Communication with the Endpoint Security subsystem failed.
- [var ES_NEW_CLIENT_RESULT_ERR_INVALID_ARGUMENT: es_new_client_result_t](es_new_client_result_err_invalid_argument.md)
  The attempt to create a new client contained one or more invalid arguments.
- [var ES_NEW_CLIENT_RESULT_ERR_NOT_ENTITLED: es_new_client_result_t](es_new_client_result_err_not_entitled.md)
  The caller isn’t properly entitled to connect to Endpoint Security.
- [var ES_NEW_CLIENT_RESULT_ERR_NOT_PERMITTED: es_new_client_result_t](es_new_client_result_err_not_permitted.md)
  The caller isn’t permitted to connect to Endpoint Security.
- [var ES_NEW_CLIENT_RESULT_ERR_NOT_PRIVILEGED: es_new_client_result_t](es_new_client_result_err_not_privileged.md)
  The caller isn’t running as root.
- [var ES_NEW_CLIENT_RESULT_ERR_TOO_MANY_CLIENTS: es_new_client_result_t](es_new_client_result_err_too_many_clients.md)
  The caller has reached the maximum allowed number of simultaneously connected clients.
### Initializers
- [init(UInt32)](es_new_client_result_t/init(_:).md)
- [init(rawValue: UInt32)](es_new_client_result_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_new_client_result_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func es_new_client(UnsafeMutablePointer<OpaquePointer?>, es_handler_block_t) -> es_new_client_result_t](es_new_client(_:_:).md)
  Creates a new client instance and connects it to the Endpoint Security system.
- [typealias es_handler_block_t](es_handler_block_t.md)
  A block that handles a message received from Endpoint Security.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_new_client_result_t)*