# SHSession.Result

**Framework**: ShazamKit  
**Kind**: enum

Identifies the result from an asynchronous sequence result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@frozen
enum Result
```

## Topics

### Constants
- [SHSession.Result.match(_:)](shsession/result/match(_:).md)
  A type that indicates a session match.
- [SHSession.Result.noMatch(_:)](shsession/result/nomatch(_:).md)
  A type that indicates there’s no match for the signature.
- [case error(any Error, SHSignature)](shsession/result/error(_:_:).md)
  A type that indicates a session error.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func result(from: SHSignature) async -> SHSession.Result](shsession/result(from:).md)
  Performs an asynchronous match with a signature you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/result)*