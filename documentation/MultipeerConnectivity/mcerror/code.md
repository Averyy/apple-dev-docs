# MCError.Code

**Framework**: Multipeer Connectivity  
**Kind**: enum  
**Role**: Enumeration

Error codes found in [`MCErrorDomain`](../mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.

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
enum Code
```

```c
enum MCErrorCode : NSInteger;
```

## Topics

### Constants
- [MCError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
- [MCError.Code.notConnected](./code/notconnected.md)
  Your app attempted to send data to a peer that is not connected.
- [MCError.Code.invalidParameter](./code/invalidparameter.md)
  Your app passed an invalid value as a parameter.
- [MCError.Code.unsupported](./code/unsupported.md)
  The operation is unsupported. For example, this error is returned if you call [`sendResource(at:withName:toPeer:withCompletionHandler:)`](../mcsession/sendresource%28at,withname,topeer,withcompletionhandler%29.md) with a URL that is neither a local file nor a web URL.
- [MCError.Code.timedOut](./code/timedout.md)
  The connection attempt timed out.
- [MCError.Code.cancelled](./code/cancelled.md)
  The operation was cancelled by the user.
- [MCError.Code.unavailable](./code/unavailable.md)
  Multipeer connectivity is currently unavailable.
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

### Constants
- [enum MCSessionSendDataMode](../mcsessionsenddatamode.md)
  Indicates whether delivery of data should be guaranteed.
- [enum MCSessionState](../mcsessionstate.md)
  Indicates the current state of a given peer within a session.
- [enum MCEncryptionPreference](../mcencryptionpreference.md)
  Indicates whether a session should use encryption when communicating with nearby peers.
- [Multipeer Connectivity Error Domain](../multipeer_connectivity_error_domain.md)
  The error domain for errors specific to Multipeer Connectivity.
- [Minimum and Maximum Supported Peers](../minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcerror/code)*