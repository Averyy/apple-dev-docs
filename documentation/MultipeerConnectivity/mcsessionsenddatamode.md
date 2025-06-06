# MCSessionSendDataMode

**Framework**: Multipeer Connectivity  
**Kind**: enum

Indicates whether delivery of data should be guaranteed.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MCSessionSendDataMode
```

## Topics

### Constants
- [MCSessionSendDataMode.reliable](mcsessionsenddatamode/reliable.md)
  The framework should guarantee delivery of each message, enqueueing and retransmitting data as needed, and ensuring in-order delivery.
- [MCSessionSendDataMode.unreliable](mcsessionsenddatamode/unreliable.md)
  Messages to peers should be sent immediately without socket-level queueing. If a message cannot be sent immediately, it should be dropped. The order of messages is not guaranteed.
### Initializers
- [init?(rawValue: Int)](mcsessionsenddatamode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MCSessionState](mcsessionstate.md)
  Indicates the current state of a given peer within a session.
- [enum MCEncryptionPreference](mcencryptionpreference.md)
  Indicates whether a session should use encryption when communicating with nearby peers.
- [MCError.Code](mcerror/code.md)
  Error codes found in [`MCErrorDomain`](mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.
- [Multipeer Connectivity Error Domain](multipeer_connectivity_error_domain.md)
  The error domain for errors specific to Multipeer Connectivity.
- [Minimum and Maximum Supported Peers](minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode)*