# FSSeekRegionResult

**Framework**: FSKit  
**Kind**: class

A seek-region result.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSSeekRegionResult
```

#### Overview

Use this type in your implementation of [`seek(within:from:region:context:replyHandler:)`](fsvolume/seekregionhandler/seek(within:from:region:context:replyhandler:).md).

## Topics

### Creating a seek-region result
- [init(returnedOffset: off_t)](fsseekregionresult/init(returnedoffset:).md)
  Creates a result for a region-seeking operation.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func seek(within: FSItem, from: off_t, region: FSVolume.SeekRegion, context: FSContext, replyHandler: (FSSeekRegionResult?, (any Error)?) -> Void)](fsvolume/seekregionhandler/seek(within:from:region:context:replyhandler:).md)
  Find the next offset of hole or data region greater than or equal to the supplied offset
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.SeekRegion](fsvolume/seekregion.md)
  Types of region for seek operations
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsseekregionresult)*