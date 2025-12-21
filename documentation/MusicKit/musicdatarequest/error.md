# MusicDataRequest.Error

**Framework**: MusicKit  
**Kind**: struct

An error that the Apple Music API returns.

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
struct Error
```

## Topics

### Instance Properties
- [let code: Int](musicdatarequest/error/code.md)
  The specific code for the underlying cause of the error.
- [let detailText: String](musicdatarequest/error/detailtext.md)
  Additional detailed information about the cause of the error.
- [let id: String](musicdatarequest/error/id.md)
  The identifier for the error.
- [let originalResponse: MusicDataResponse](musicdatarequest/error/originalresponse.md)
  The original response that contains the error.
- [let source: MusicDataRequest.Error.Source?](musicdatarequest/error/source-swift.property.md)
  The source of the error.
- [let status: Int](musicdatarequest/error/status.md)
  The HTTP status code for the error.
- [let title: String](musicdatarequest/error/title.md)
  A developer-friendly title for the error.
### Enumerations
- [MusicDataRequest.Error.Source](musicdatarequest/error/source-swift.enum.md)
  A representation of the source of an error from Apple Music API.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicdatarequest/error)*