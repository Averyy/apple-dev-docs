# es_client_t

**Framework**: Endpoint Security  
**Kind**: typealias  
**Role**: Type Alias

An opaque type that stores the Endpoint Security client state.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
typedef struct es_client_s es_client_t;
```

## See Also

### Creating a Client
- [func es_new_client(UnsafeMutablePointer<OpaquePointer?>, es_handler_block_t) -> es_new_client_result_t](./es_new_client%28_,_%29.md)
  Creates a new client instance and connects it to the Endpoint Security system.
- [typealias es_handler_block_t](./es_handler_block_t.md)
  A block that handles a message received from Endpoint Security.
- [struct es_new_client_result_t](./es_new_client_result_t.md)
  The result of an attempt to create a new client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_client_t)*