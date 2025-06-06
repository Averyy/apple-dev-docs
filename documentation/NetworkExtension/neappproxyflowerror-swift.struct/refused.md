# refused

**Framework**: Network Extension  
**Kind**: property

Connecting the flow to its remote endpoint failed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var refused: NEAppProxyFlowError.Code { get }
```

## See Also

- [static var notConnected: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/notconnected.md)
  The flow is not fully opened.
- [static var peerReset: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/peerreset.md)
  The remote peer closed the flow.
- [static var hostUnreachable: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/hostunreachable.md)
  An attempt to reach the remote endpoint of the flow failed.
- [static var invalidArgument: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/invalidargument.md)
  A proxy flow method received an invalid argument.
- [static var aborted: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/aborted.md)
  The flow was aborted.
- [static var timedOut: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/timedout.md)
  The flow timed out.
- [static var `internal`: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/internal.md)
  An internal error occurred while handling the flow.
- [static var datagramTooLarge: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/datagramtoolarge.md)
  A caller attempted to write a datagram that was larger than the socket’s receive window.
- [static var readAlreadyPending: NEAppProxyFlowError.Code](neappproxyflowerror-swift.struct/readalreadypending.md)
  A read operation on the flow is already pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflowerror-swift.struct/refused)*