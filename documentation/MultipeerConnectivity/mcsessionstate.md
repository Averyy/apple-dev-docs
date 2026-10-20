# MCSessionState

**Framework**: Multipeer Connectivity  
**Kind**: enum  
**Role**: Enumeration

Indicates the current state of a given peer within a session.

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
enum MCSessionState
```

```c
enum MCSessionState : NSInteger;
```

## Topics

### Constants
- [MCSessionState.notConnected](./mcsessionstate/notconnected.md)
  The peer is not (or is no longer) in this session.
- [MCSessionState.connecting](./mcsessionstate/connecting.md)
  A connection to the peer is currently being established.
- [MCSessionState.connected](./mcsessionstate/connected.md)
  The peer is connected to this session.
### Initializers
- [init?(rawValue: Int)](./mcsessionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum MCSessionSendDataMode](./mcsessionsenddatamode.md)
  Indicates whether delivery of data should be guaranteed.
- [enum MCEncryptionPreference](./mcencryptionpreference.md)
  Indicates whether a session should use encryption when communicating with nearby peers.
- [MCError.Code](./mcerror/code.md)
  Error codes found in [`MCErrorDomain`](./mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.
- [Multipeer Connectivity Error Domain](./multipeer_connectivity_error_domain.md)
  The error domain for errors specific to Multipeer Connectivity.
- [Minimum and Maximum Supported Peers](./minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate)*