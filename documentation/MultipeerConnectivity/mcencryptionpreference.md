# MCEncryptionPreference

**Framework**: Multipeer Connectivity  
**Kind**: enum  
**Role**: Enumeration

Indicates whether a session should use encryption when communicating with nearby peers.

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
enum MCEncryptionPreference
```

```c
enum MCEncryptionPreference : NSInteger;
```

## Topics

### Constants
- [MCEncryptionPreference.optional](./mcencryptionpreference/optional.md)
  The session prefers to use encryption, but accepts unencrypted connections. A connection uses encryption when all the peers choose either [`MCEncryptionPreference.optional`](./mcencryptionpreference/optional.md) or [`MCEncryptionPreference.required`](./mcencryptionpreference/required.md). If some peers choose [`MCEncryptionPreference.none`](./mcencryptionpreference/none.md), then the session will not be encrypted. For this reason, if some peers running your app can be configured without encryption, you should always assume that the session is unencrypted.
- [MCEncryptionPreference.required](./mcencryptionpreference/required.md)
  The session requires encryption.
- [MCEncryptionPreference.none](./mcencryptionpreference/none.md)
  The session should not be encrypted.
### Initializers
- [init?(rawValue: Int)](./mcencryptionpreference/init%28rawvalue%29.md)

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
- [enum MCSessionState](./mcsessionstate.md)
  Indicates the current state of a given peer within a session.
- [MCError.Code](./mcerror/code.md)
  Error codes found in [`MCErrorDomain`](./mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.
- [Multipeer Connectivity Error Domain](./multipeer_connectivity_error_domain.md)
  The error domain for errors specific to Multipeer Connectivity.
- [Minimum and Maximum Supported Peers](./minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference)*