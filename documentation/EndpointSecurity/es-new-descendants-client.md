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

The returned client receives notify events for the calling process and auth+notify events for its descendant processes (the entire subtree rooted at the calling process). This includes descendants that already exist at the time the client is created as well as any forked or exec’d afterward, recursively. All other processes are invisible.

Process muting works, but only for processes that are already in the descendant subtree. es_mute_process / es_mute_process_events (and their unmute counterparts) succeed for a process the client can already observe and return ES_RETURN_ERROR for any process outside the subtree; the client cannot reach a process it was never allowed to see. Path muting and target-path muting work normally.

> **Note**: Requires the com.apple.developer.endpoint-security.client entitlement.

> **Note**: Does NOT require root privilege.

> **Note**: Does NOT require TCC approval.

> **Note**: Events will be delivered when a descendant submits the event or instigates it

## Parameters

- `client`: Out param. On success, set to the newly created es_client_t.
- `handler`: The handler block invoked for each event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_new_descendants_client(_:_:))*