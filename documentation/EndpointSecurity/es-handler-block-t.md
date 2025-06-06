# es_handler_block_t

**Framework**: Endpoint Security  
**Kind**: typealias

A block that handles a message received from Endpoint Security.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias es_handler_block_t = (OpaquePointer, UnsafePointer<es_message_t>) -> Void
```

#### Discussion

The block receives two parameters:

- The client that receives the event, as an [`es_client_t`](es_client_t.md) pointer. You pass this client to any `es_respond`-prefixed functions that you call in the handler.
- The message to handle, as an [`es_message_t`](es_message_t.md) pointer.

You implement the handler by inspecting the message and deciding how to respond to it. For example, your handler might receive a message with [`event_type`](es_message_t/event_type.md) [`ES_EVENT_TYPE_AUTH_RENAME`](es_event_type_auth_rename.md), indicating that the system wants authorization before renaming a file. Your handler would call [`es_respond_auth_result(_:_:_:_:)`](es_respond_auth_result(_:_:_:_:).md) to permit or deny the renaming.

## See Also

- [func es_new_client(UnsafeMutablePointer<OpaquePointer?>, es_handler_block_t) -> es_new_client_result_t](es_new_client(_:_:).md)
  Creates a new client instance and connects it to the Endpoint Security system.
- [struct es_new_client_result_t](es_new_client_result_t.md)
  The result of an attempt to create a new client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_handler_block_t)*