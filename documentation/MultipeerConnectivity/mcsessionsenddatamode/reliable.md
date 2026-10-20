# MCSessionSendDataMode.reliable

**Framework**: Multipeer Connectivity  
**Kind**: case  
**Role**: Case

The framework should guarantee delivery of each message, enqueueing and retransmitting data as needed, and ensuring in-order delivery.

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
case reliable
```

```c
MCSessionSendDataReliable
```

#### Discussion

Use this message type for application-critical data.

## See Also

### Constants
- [MCSessionSendDataMode.unreliable](./unreliable.md)
  Messages to peers should be sent immediately without socket-level queueing. If a message cannot be sent immediately, it should be dropped. The order of messages is not guaranteed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/reliable)*