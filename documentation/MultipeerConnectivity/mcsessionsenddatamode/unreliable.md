# MCSessionSendDataMode.unreliable

**Framework**: Multipeer Connectivity  
**Kind**: case

Messages to peers should be sent immediately without socket-level queueing. If a message cannot be sent immediately, it should be dropped. The order of messages is not guaranteed.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case unreliable
```

#### Discussion

Use this message type for data that ceases to be relevant if delayed, such as real-time gaming data.

## See Also

- [MCSessionSendDataMode.reliable](mcsessionsenddatamode/reliable.md)
  The framework should guarantee delivery of each message, enqueueing and retransmitting data as needed, and ensuring in-order delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/unreliable)*