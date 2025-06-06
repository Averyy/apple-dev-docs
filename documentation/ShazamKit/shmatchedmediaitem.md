# SHMatchedMediaItem

**Framework**: ShazamKit  
**Kind**: class

An object that represents the metadata for a matched reference signature.

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
class SHMatchedMediaItem
```

#### Overview

To access properties for custom media items, use subscripting. For more information, see [`SHMediaItem`](shmediaitem.md).

## Topics

### Reading information about the match
- [var matchOffset: TimeInterval](shmatchedmediaitem/matchoffset.md)
  The timecode in the reference recording that matches the start of the query, in seconds.
- [var predictedCurrentMatchOffset: TimeInterval](shmatchedmediaitem/predictedcurrentmatchoffset.md)
  The updated timecode in the reference recording that matches the current playback position of the query audio, in seconds.
- [var frequencySkew: Float](shmatchedmediaitem/frequencyskew.md)
  A multiple for the difference in frequency between the matched audio and the query audio.
### Instance Properties
- [var confidence: Float](shmatchedmediaitem/confidence.md)
  The level of confidence in the match result.

## Relationships

### Inherits From
- [SHMediaItem](shmediaitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [class SHMatch](shmatch.md)
  An object that represents the catalog media items that match a query.
- [class SHMediaItem](shmediaitem.md)
  An object that represents the metadata for a reference signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmatchedmediaitem)*