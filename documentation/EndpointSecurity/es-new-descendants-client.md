# es_new_descendants_client(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Create a new ES client scoped to descendant processes only.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_new_descendants_client(_ client: UnsafeMutablePointer<OpaquePointer?>, _ handler: @escaping es_handler_block_t) -> es_new_client_result_t
```

#### Return Value

Es_new_client_result_t indicating success or a specific error.

#### Discussion

The returned client receives notify events for the calling process and auth+notify events for descendant processes (forked or exec’d after creation, recursively). All other processes are invisible.

Process muting APIs are not available and return ES_RETURN_ERROR. Path muting and target-path muting work normally.

> **Note**: Requires the com.apple.developer.endpoint-security.client entitlement.

> **Note**: Does NOT require root privilege.

> **Note**: Does NOT require TCC approval.

> **Note**: Events will be delivered when a descendant submits the event or instigates it

## Parameters

- `client`: Out param. On success, set to the newly created es_client_t.
- `handler`: The handler block invoked for each event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_new_descendants_client(_:_:))*