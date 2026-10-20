# NWUDPSessionState

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_state_t`](../Network/nw_connection_state_t.md) type from the [Network](../Network/Network.md) framework instead.

## Declaration

```swift
enum NWUDPSessionState
```

```c
enum NWUDPSessionState : NSInteger;
```

## Topics

### Session States
- [NWUDPSessionState.invalid](./nwudpsessionstate/invalid.md)
  The session is in an invalid or uninitialized state.
- [NWUDPSessionState.waiting](./nwudpsessionstate/waiting.md)
  The session is waiting for better conditions before attempting to make the session ready.
- [NWUDPSessionState.preparing](./nwudpsessionstate/preparing.md)
  The remote endpoint is being resolved.
- [NWUDPSessionState.ready](./nwudpsessionstate/ready.md)
  The session is ready for reading and writing data.
- [NWUDPSessionState.failed](./nwudpsessionstate/failed.md)
  None of the currently resolved endpoints can be used at this time, either due to problems with the path or the client rejecting the endpoints.
- [NWUDPSessionState.cancelled](./nwudpsessionstate/cancelled.md)
  The session has been cancelled by the client calling `cancel`.
### Initializers
- [init?(rawValue: Int)](./nwudpsessionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Monitoring the session state
- [var state: NWUDPSessionState](./nwudpsession/state.md)
  The current state of the UDP session.
- [var isViable: Bool](./nwudpsession/isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsessionstate)*