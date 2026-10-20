# SHSession.Result

**Framework**: ShazamKit  
**Kind**: enum  
**Role**: Enumeration

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
- [SHSession.Result.match(_:)](./result/match%28_%29.md)
  A type that indicates a session match.
- [SHSession.Result.noMatch(_:)](./result/nomatch%28_%29.md)
  A type that indicates there’s no match for the signature.
- [case error(any Error, SHSignature)](./result/error%28_,_%29.md)
  A type that indicates a session error.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Returning queries
- [func result(from: SHSignature) async -> SHSession.Result](./result%28from%29.md)
  Performs an asynchronous match with a signature you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession/result)*