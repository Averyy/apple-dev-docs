# es_new_client(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Creates a new client instance and connects it to the Endpoint Security system.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_new_client(_ client: UnsafeMutablePointer<OpaquePointer?>, _ handler: @escaping es_handler_block_t) -> es_new_client_result_t
```

#### Return Value

A result value indicating that indicates either success or the reason why client initialization failed.

#### Discussion

The handler block receives messages serially, and in the order the system delivers them. Returning control from the handler causes Endpoint Security to dequeue the next available message.

You can respond to a message out of order by returning control before calling one of the `es_respond`-prefixed functions. For out-of-order responding, your handler must copy the message with [`es_copy_message(_:)`](es_copy_message(_:).md).

To create a client, your app must have the `com.apple.developer.endpoint-security.client` entitlement. The user also needs to approve your app with Transparency, Consent, and Control (TCC) mechanisms. The user does this in the Security and Privacy pane of System Preferences, by adding the app to Full Disk Access.

When you no longer need to receive Endpoint Security messages, destroy the client with [`es_delete_client(_:)`](es_delete_client(_:).md) to free resources.

## Parameters

- `client`: A pointer to receive the new client instance.
- `handler`: The handler to run on all messages sent to this client.

## See Also

- [com.apple.developer.endpoint-security.client](../BundleResources/Entitlements/com.apple.developer.endpoint-security.client.md)
  The entitlement required to monitor system events for potentially malicious activity.
- [typealias es_handler_block_t](es_handler_block_t.md)
  A block that handles a message received from Endpoint Security.
- [struct es_new_client_result_t](es_new_client_result_t.md)
  The result of an attempt to create a new client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_new_client(_:_:))*