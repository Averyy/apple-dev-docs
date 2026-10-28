# FSSeekRegionResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A seek-region result.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSSeekRegionResult
```

```objc
@interface FSSeekRegionResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`seek(within:from:region:context:replyHandler:)`](./fsvolume/seekregionhandler/seek%28within,from,region,context,replyhandler%29.md).

## Topics

### Creating a seek-region result
- [init(returnedOffset: off_t)](./fsseekregionresult/init%28returnedoffset%29.md)
  Creates a result for a region-seeking operation.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Performing seek
- [func seek(within: FSItem, from: off_t, region: FSVolume.SeekRegion, context: FSContext, replyHandler: (FSSeekRegionResult?, (any Error)?) -> Void)](./fsvolume/seekregionhandler/seek%28within,from,region,context,replyhandler%29.md)
  Find the next offset of hole or data region greater than or equal to the supplied offset
- [class FSItem](./fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.SeekRegion](./fsvolume/seekregion.md)
  Types of region for seek operations
- [class FSContext](./fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsseekregionresult)*