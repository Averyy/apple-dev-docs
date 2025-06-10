# SHError

**Framework**: ShazamKit  
**Kind**: struct

An error type that you create, or the system creates, to indicate problems with a catalog, match attempt, or signature, or when saving to a user’s Shazam library.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SHError
```

## Topics

### Inspecting an error
- [SHError.Code](sherror/code.md)
  Codes for the errors that Shazam produces.
- [Error Constants](error-constants.md)
  Error code constants for framework operations.
### Type Properties
- [static var errorDomain: String](sherror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/sherror)*