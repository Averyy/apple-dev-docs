# seek(within:from:region:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Find the next offset of hole or data region greater than or equal to the supplied offset

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func seek(within item: FSItem, from offset: off_t, region: FSVolume.SeekRegion, context: FSContext) async throws -> FSSeekRegionResult
```

## Parameters

- `item`: The item for which to seek.
- `offset`: The offset from which to seek.
- `region`: The region to seek.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If seek succeeds, pass an instance of [`FSSeekRegionResult`](fsseekregionresult.md) containing the offset of the requested region greater than or equal to the supplied offset, along with a `nil` error. If seek fails, pass the relevant error as the second parameter; FSKit ignores the [`FSSeekRegionResult`](fsseekregionresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.SeekRegion](fsvolume/seekregion.md)
  Types of region for seek operations
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSSeekRegionResult](fsseekregionresult.md)
  A seek-region result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregionhandler/seek(within:from:region:context:replyhandler:))*