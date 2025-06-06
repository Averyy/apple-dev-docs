# NEAppProxyFlowError.Code.peerReset

**Framework**: Network Extension  
**Kind**: case

The remote peer closed the flow.

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
case peerReset
```

## See Also

- [NEAppProxyFlowError.Code.notConnected](neappproxyflowerror-swift.struct/code/notconnected.md)
  The flow is not fully opened.
- [NEAppProxyFlowError.Code.hostUnreachable](neappproxyflowerror-swift.struct/code/hostunreachable.md)
  An attempt to reach the remote endpoint of the flow failed.
- [NEAppProxyFlowError.Code.invalidArgument](neappproxyflowerror-swift.struct/code/invalidargument.md)
  A proxy flow method received an invalid argument.
- [NEAppProxyFlowError.Code.aborted](neappproxyflowerror-swift.struct/code/aborted.md)
  The flow was aborted.
- [NEAppProxyFlowError.Code.refused](neappproxyflowerror-swift.struct/code/refused.md)
  Connecting the flow to its remote endpoint failed.
- [NEAppProxyFlowError.Code.timedOut](neappproxyflowerror-swift.struct/code/timedout.md)
  The flow timed out.
- [NEAppProxyFlowError.Code.internal](neappproxyflowerror-swift.struct/code/internal.md)
  An internal error occurred while handling the flow.
- [NEAppProxyFlowError.Code.datagramTooLarge](neappproxyflowerror-swift.struct/code/datagramtoolarge.md)
  A caller attempted to write a datagram that was larger than the socket’s receive window.
- [NEAppProxyFlowError.Code.readAlreadyPending](neappproxyflowerror-swift.struct/code/readalreadypending.md)
  A read operation on the flow is already pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflowerror-swift.struct/code/peerreset)*