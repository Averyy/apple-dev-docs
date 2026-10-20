# MCSessionSendDataMode.unreliable

**Framework**: Multipeer Connectivity  
**Kind**: case  
**Role**: Case

Messages to peers should be sent immediately without socket-level queueing. If a message cannot be sent immediately, it should be dropped. The order of messages is not guaranteed.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
case unreliable
```

```c
MCSessionSendDataUnreliable
```

#### Discussion

Use this message type for data that ceases to be relevant if delayed, such as real-time gaming data.

## See Also

### Constants
- [MCSessionSendDataMode.reliable](./reliable.md)
  The framework should guarantee delivery of each message, enqueueing and retransmitting data as needed, and ensuring in-order delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/unreliable)*