# MusicUnderstandingError

**Framework**: Music Understanding  
**Kind**: enum

An error that occurs during a music understanding session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum MusicUnderstandingError
```

## Topics

### Types of error cases
- [MusicUnderstandingError.emptyAnalysisSet](musicunderstandingerror/emptyanalysisset.md)
  The error that occurs when someone requests and analysis of an empty analysis set.
- [MusicUnderstandingError.internalError](musicunderstandingerror/internalerror.md)
  The error that occurs when an unexpected internal failure prevents the session from completing.
- [MusicUnderstandingError.invalidAsset](musicunderstandingerror/invalidasset.md)
  The error that occurs when someone initializes a session with an invalid asset.
- [MusicUnderstandingError.sessionInProgress](musicunderstandingerror/sessioninprogress.md)
  The error that occurs when someone requests analysis while a session is already in progress.
### Enumeration Cases
- [MusicUnderstandingError.hasProtectedContent](musicunderstandingerror/hasprotectedcontent.md)
  The error that occurs when a session is initialized with an `AVAsset` whose content is protected by DRM and cannot be decoded for analysis.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingerror)*