# NEAppProxyFlowError.Code

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

Error codes that the app proxy flow API declares.

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
enum Code
```

```c
enum NEAppProxyFlowError : NSInteger;
```

## Topics

### Error Codes
- [NEAppProxyFlowError.Code.notConnected](./code/notconnected.md)
  The flow is not fully opened.
- [NEAppProxyFlowError.Code.peerReset](./code/peerreset.md)
  The remote peer closed the flow.
- [NEAppProxyFlowError.Code.hostUnreachable](./code/hostunreachable.md)
  An attempt to reach the remote endpoint of the flow failed.
- [NEAppProxyFlowError.Code.invalidArgument](./code/invalidargument.md)
  A proxy flow method received an invalid argument.
- [NEAppProxyFlowError.Code.aborted](./code/aborted.md)
  The flow was aborted.
- [NEAppProxyFlowError.Code.refused](./code/refused.md)
  Connecting the flow to its remote endpoint failed.
- [NEAppProxyFlowError.Code.timedOut](./code/timedout.md)
  The flow timed out.
- [NEAppProxyFlowError.Code.internal](./code/internal.md)
  An internal error occurred while handling the flow.
- [NEAppProxyFlowError.Code.datagramTooLarge](./code/datagramtoolarge.md)
  A caller attempted to write a datagram that was larger than the socket’s receive window.
- [NEAppProxyFlowError.Code.readAlreadyPending](./code/readalreadypending.md)
  A read operation on the flow is already pending.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct NEAppProxyFlowError](../neappproxyflowerror-swift.struct.md)
  An error that the app proxy flow encounters.
- [let NEAppProxyErrorDomain: String](../neappproxyerrordomain.md)
  The domain used for app proxy errors.
- [struct NEAppProxyFlowError](../neappproxyflowerror-swift.struct.md)
  An error that the app proxy flow encounters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflowerror-swift.struct/code)*