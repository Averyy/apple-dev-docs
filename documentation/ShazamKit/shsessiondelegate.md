# SHSessionDelegate

**Framework**: ShazamKit  
**Kind**: protocol

Methods that the session calls with the result of a match request.

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
protocol SHSessionDelegate : NSObjectProtocol
```

## Topics

### Handling matches
- [func session(SHSession, didFind: SHMatch)](shsessiondelegate/session(_:didfind:).md)
  Tells the delegate that the query signature matches an item in the catalog.
- [func session(SHSession, didNotFindMatchFor: SHSignature, error: (any Error)?)](shsessiondelegate/session(_:didnotfindmatchfor:error:).md)
  Tells the delegate that the query signature doesn’t match an item in the catalog, or that there’s an error.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SHSession](shsession.md)
  An object that matches a specific audio recording when a segment of that recording is part of captured sound in the Shazam catalog or your custom catalog.
- [class SHManagedSession](shmanagedsession.md)
  An object that records and matches a recording with captured sound in the Shazam catalog or your custom catalog.
- [class SHMatch](shmatch.md)
  An object that represents the catalog media items that match a query.
- [class SHMatchedMediaItem](shmatchedmediaitem.md)
  An object that represents the metadata for a matched reference signature.
- [class SHMediaItem](shmediaitem.md)
  An object that represents the metadata for a reference signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsessiondelegate)*