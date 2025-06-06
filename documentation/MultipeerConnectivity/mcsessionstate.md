# MCSessionState

**Framework**: Multipeer Connectivity  
**Kind**: enum

Indicates the current state of a given peer within a session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MCSessionState
```

## Topics

### Constants
- [MCSessionState.notConnected](mcsessionstate/notconnected.md)
  The peer is not (or is no longer) in this session.
- [MCSessionState.connecting](mcsessionstate/connecting.md)
  A connection to the peer is currently being established.
- [MCSessionState.connected](mcsessionstate/connected.md)
  The peer is connected to this session.
### Initializers
- [init?(rawValue: Int)](mcsessionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MCSessionSendDataMode](mcsessionsenddatamode.md)
  Indicates whether delivery of data should be guaranteed.
- [enum MCEncryptionPreference](mcencryptionpreference.md)
  Indicates whether a session should use encryption when communicating with nearby peers.
- [MCError.Code](mcerror/code.md)
  Error codes found in [`MCErrorDomain`](mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.
- [Multipeer Connectivity Error Domain](multipeer_connectivity_error_domain.md)
  The error domain for errors specific to Multipeer Connectivity.
- [Minimum and Maximum Supported Peers](minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate)*