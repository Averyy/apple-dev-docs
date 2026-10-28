# SHMatch

**Framework**: ShazamKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface SHMatch : NSObject
```

## Overview

A single query signature may match more than one reference signature. In addition, one reference signature may map to many media items.

## Topics

### Reading match information
- [var mediaItems: [SHMatchedMediaItem]](./shmatch/mediaitems.md)
  An array of the media items in the catalog that match the query signature, in order of the quality of the match.
- [var querySignature: SHSignature](./shmatch/querysignature.md)
  The query signature for the match.
### Initializers
- [init?(coder: NSCoder)](./shmatch/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Match audio
- [class SHSession](./shsession.md)
  An object that matches a specific audio recording when a segment of that recording is part of captured sound in the Shazam catalog or your custom catalog.
- [class SHManagedSession](./shmanagedsession.md)
  An object that records and matches a recording with captured sound in the Shazam catalog or your custom catalog.
- [protocol SHSessionDelegate](./shsessiondelegate.md)
  Methods that the session calls with the result of a match request.
- [class SHMatchedMediaItem](./shmatchedmediaitem.md)
  An object that represents the metadata for a matched reference signature.
- [class SHMediaItem](./shmediaitem.md)
  An object that represents the metadata for a reference signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmatch)*