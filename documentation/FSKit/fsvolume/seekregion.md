# FSVolume.SeekRegion

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

Types of region for seek operations

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum SeekRegion
```

```c
enum FSSeekRegion : NSUInteger;
```

## Topics

### Seek region types
- [FSVolume.SeekRegion.data](./seekregion/data.md)
  Seek the next data region.
- [FSVolume.SeekRegion.hole](./seekregion/hole.md)
  Seek the next hole region.
### Initializers
- [init?(rawValue: UInt)](./seekregion/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing seek
- [func seek(within: FSItem, from: off_t, region: FSVolume.SeekRegion, context: FSContext, replyHandler: (FSSeekRegionResult?, (any Error)?) -> Void)](./seekregionhandler/seek%28within,from,region,context,replyhandler%29.md)
  Find the next offset of hole or data region greater than or equal to the supplied offset
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](../fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSSeekRegionResult](../fsseekregionresult.md)
  A seek-region result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregion)*