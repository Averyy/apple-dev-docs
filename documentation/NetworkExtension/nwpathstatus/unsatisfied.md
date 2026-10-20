# NWPathStatus.unsatisfied

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

The path for network connections is not available, either due to lack of network connectivity or being prohibited by system policy.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_status_t`](../../Network/nw_path_status_t.md) type from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
case unsatisfied
```

```c
NWPathStatusUnsatisfied
```

## See Also

### Path Statuses
- [NWPathStatus.invalid](./invalid.md)
  The path cannot be evaluated.
- [NWPathStatus.satisfied](./satisfied.md)
  The path is ready to be used for network connections.
- [NWPathStatus.satisfiable](./satisfiable.md)
  The path is not currently satisfied, but may become satisfied upon a connection attempt. This can be due to a service, such as a VPN or a cellular data connection not being activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpathstatus/unsatisfied)*