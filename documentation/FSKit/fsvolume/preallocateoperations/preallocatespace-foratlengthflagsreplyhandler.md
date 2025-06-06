# preallocateSpace(for:at:length:flags:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Prealocates disk space for the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func preallocateSpace(for item: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags) async throws -> Int
```

## Parameters

- `item`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass the amount of bytes allocated and a   error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores any byte count in this case. For an   Swift implementation, there’s no reply handler; simply return the allocated byte count or throw an error.

## See Also

- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateoperations/preallocatespace(for:at:length:flags:replyhandler:))*