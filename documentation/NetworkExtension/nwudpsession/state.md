# state

**Framework**: Network Extension  
**Kind**: property

The current state of the UDP session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var state: NWUDPSessionState { get }
```

#### Discussion

Use Key-Value Observing (KVO) to monitor the state. If the state is `NWUDPSessionStateReady`, then the connection is eligible for reading and writing. The state will be `NWUDPSessionStateFailed` if the endpoint could not be resolved, or all endpoints have been rejected. For information about KVO, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [enum NWUDPSessionState](nwudpsessionstate.md)
- [var isViable: Bool](nwudpsession/isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/state)*