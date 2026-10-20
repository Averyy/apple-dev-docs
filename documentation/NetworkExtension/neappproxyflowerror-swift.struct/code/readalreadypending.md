# NEAppProxyFlowError.Code.readAlreadyPending

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

A read operation on the flow is already pending.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
case readAlreadyPending
```

```c
NEAppProxyFlowErrorReadAlreadyPending
```

## See Also

### Error Codes
- [NEAppProxyFlowError.Code.notConnected](./notconnected.md)
  The flow is not fully opened.
- [NEAppProxyFlowError.Code.peerReset](./peerreset.md)
  The remote peer closed the flow.
- [NEAppProxyFlowError.Code.hostUnreachable](./hostunreachable.md)
  An attempt to reach the remote endpoint of the flow failed.
- [NEAppProxyFlowError.Code.invalidArgument](./invalidargument.md)
  A proxy flow method received an invalid argument.
- [NEAppProxyFlowError.Code.aborted](./aborted.md)
  The flow was aborted.
- [NEAppProxyFlowError.Code.refused](./refused.md)
  Connecting the flow to its remote endpoint failed.
- [NEAppProxyFlowError.Code.timedOut](./timedout.md)
  The flow timed out.
- [NEAppProxyFlowError.Code.internal](./internal.md)
  An internal error occurred while handling the flow.
- [NEAppProxyFlowError.Code.datagramTooLarge](./datagramtoolarge.md)
  A caller attempted to write a datagram that was larger than the socket’s receive window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflowerror-swift.struct/code/readalreadypending)*