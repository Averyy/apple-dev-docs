# SHMatch

**Framework**: ShazamKit  
**Kind**: class

An object that represents the catalog media items that match a query.

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
class SHMatch
```

#### Overview

A single query signature may match more than one reference signature. In addition, one reference signature may map to many media items.

## Topics

### Reading match information
- [var mediaItems: [SHMatchedMediaItem]](shmatch/mediaitems.md)
  An array of the media items in the catalog that match the query signature, in order of the quality of the match.
- [var querySignature: SHSignature](shmatch/querysignature.md)
  The query signature for the match.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class SHSession](shsession.md)
  An object that matches a specific audio recording when a segment of that recording is part of captured sound in the Shazam catalog or your custom catalog.
- [class SHManagedSession](shmanagedsession.md)
  An object that records and matches a recording with captured sound in the Shazam catalog or your custom catalog.
- [protocol SHSessionDelegate](shsessiondelegate.md)
  Methods that the session calls with the result of a match request.
- [class SHMatchedMediaItem](shmatchedmediaitem.md)
  An object that represents the metadata for a matched reference signature.
- [class SHMediaItem](shmediaitem.md)
  An object that represents the metadata for a reference signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmatch)*