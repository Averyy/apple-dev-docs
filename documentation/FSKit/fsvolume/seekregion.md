# FSVolume.SeekRegion

**Framework**: FSKit  
**Kind**: enum

Types of region for seek operations

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum SeekRegion
```

## Topics

### Seek region types
- [FSVolume.SeekRegion.data](fsvolume/seekregion/data.md)
  Seek the next data region.
- [FSVolume.SeekRegion.hole](fsvolume/seekregion/hole.md)
  Seek the next hole region.
### Initializers
- [init?(rawValue: UInt)](fsvolume/seekregion/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func seek(within: FSItem, from: off_t, region: FSVolume.SeekRegion, context: FSContext, replyHandler: (FSSeekRegionResult?, (any Error)?) -> Void)](fsvolume/seekregionhandler/seek(within:from:region:context:replyhandler:).md)
  Find the next offset of hole or data region greater than or equal to the supplied offset
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSSeekRegionResult](fsseekregionresult.md)
  A seek-region result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregion)*