# NWUDPSessionState.failed

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

None of the currently resolved endpoints can be used at this time, either due to problems with the path or the client rejecting the endpoints.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_state_t`](../../Network/nw_connection_state_t.md) type from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
case failed
```

```c
NWUDPSessionStateFailed
```

## See Also

### Session States
- [NWUDPSessionState.invalid](./invalid.md)
  The session is in an invalid or uninitialized state.
- [NWUDPSessionState.waiting](./waiting.md)
  The session is waiting for better conditions before attempting to make the session ready.
- [NWUDPSessionState.preparing](./preparing.md)
  The remote endpoint is being resolved.
- [NWUDPSessionState.ready](./ready.md)
  The session is ready for reading and writing data.
- [NWUDPSessionState.cancelled](./cancelled.md)
  The session has been cancelled by the client calling `cancel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/failed)*