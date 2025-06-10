# NWUDPSessionState

**Framework**: Network Extension  
**Kind**: enum

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NWUDPSessionState
```

## Topics

### Session States
- [NWUDPSessionState.invalid](nwudpsessionstate/invalid.md)
  The session is in an invalid or uninitialized state.
- [NWUDPSessionState.waiting](nwudpsessionstate/waiting.md)
  The session is waiting for better conditions before attempting to make the session ready.
- [NWUDPSessionState.preparing](nwudpsessionstate/preparing.md)
  The remote endpoint is being resolved.
- [NWUDPSessionState.ready](nwudpsessionstate/ready.md)
  The session is ready for reading and writing data.
- [NWUDPSessionState.failed](nwudpsessionstate/failed.md)
  None of the currently resolved endpoints can be used at this time, either due to problems with the path or the client rejecting the endpoints.
- [NWUDPSessionState.cancelled](nwudpsessionstate/cancelled.md)
  The session has been cancelled by the client calling `cancel`.
### Initializers
- [init?(rawValue: Int)](nwudpsessionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: NWUDPSessionState](nwudpsession/state.md)
  The current state of the UDP session.
- [var isViable: Bool](nwudpsession/isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsessionstate)*