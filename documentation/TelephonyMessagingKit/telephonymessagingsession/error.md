# TelephonyMessagingSession.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration of errors that can result from operations on a messaging session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Error
```

## Topics

### Inspecting errors
- [TelephonyMessagingSession.Error.invalidSession](telephonymessagingsession/error/invalidsession.md)
  The session is invalid.
- [TelephonyMessagingSession.Error.serviceUnavailable](telephonymessagingsession/error/serviceunavailable.md)
  The service is unavailable.
- [TelephonyMessagingSession.Error.invalidArgument](telephonymessagingsession/error/invalidargument.md)
  A call used an invalid argument.
- [TelephonyMessagingSession.Error.internalError](telephonymessagingsession/error/internalerror.md)
  The session encountered an internal service error.
### Hashing
- [func hash(into: inout Hasher)](telephonymessagingsession/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](telephonymessagingsession/error/hashvalue.md)
  The hash value.
### Comparing errors
- [static func == (TelephonyMessagingSession.Error, TelephonyMessagingSession.Error) -> Bool](telephonymessagingsession/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Decodable Implementations](telephonymessagingsession/error/decodable-implementations.md)
- [Encodable Implementations](telephonymessagingsession/error/encodable-implementations.md)
- [Equatable Implementations](telephonymessagingsession/error/equatable-implementations.md)
- [Error Implementations](telephonymessagingsession/error/error-implementations.md)
- [LocalizedError Implementations](telephonymessagingsession/error/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession/error)*