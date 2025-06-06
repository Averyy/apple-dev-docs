# MCSessionSendDataMode.reliable

**Framework**: Multipeer Connectivity  
**Kind**: case

The framework should guarantee delivery of each message, enqueueing and retransmitting data as needed, and ensuring in-order delivery.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case reliable
```

#### Discussion

Use this message type for application-critical data.

## See Also

- [MCSessionSendDataMode.unreliable](mcsessionsenddatamode/unreliable.md)
  Messages to peers should be sent immediately without socket-level queueing. If a message cannot be sent immediately, it should be dropped. The order of messages is not guaranteed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/reliable)*