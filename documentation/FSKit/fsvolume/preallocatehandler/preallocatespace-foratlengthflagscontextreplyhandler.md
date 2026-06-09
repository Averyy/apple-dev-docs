# preallocateSpace(for:at:length:flags:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Preallocates disk space for the given item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func preallocateSpace(for item: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, context: FSContext) async throws -> FSPreallocateResult
```

## Parameters

- `item`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass an instance of [`FSPreallocateResult`](fspreallocateresult.md) containing the amount of bytes allocated, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the file and the volume’s updated free space, along with a `nil` error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSPreallocateResult`](fspreallocateresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateResult](fspreallocateresult.md)
  The result of a preallocate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocatehandler/preallocatespace(for:at:length:flags:context:replyhandler:))*