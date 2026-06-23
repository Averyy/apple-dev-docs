# es_exec_entitlements(_:)

**Framework**: Endpoint Security  
**Kind**: func

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func es_exec_entitlements(_ exec: UnsafePointer<es_event_exec_t>) -> xpc_object_t?
```

#### Return Value

The XPC dictionary containing all entitlements, or NULL if there are no entitlements.

#### Discussion

Get the dictionary of entitlements associated with a message containing an es_event_exec_t

> **Note**: The caller is responsible for releasing the returned object.

## Parameters

- `exec`: The es_event_exec_t being inspected


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_exec_entitlements(_:))*