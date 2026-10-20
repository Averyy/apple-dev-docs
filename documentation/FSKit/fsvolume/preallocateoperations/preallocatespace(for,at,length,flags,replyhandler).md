# preallocateSpace(for:at:length:flags:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Preallocates disk space for the given item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func preallocateSpace(for item: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags, replyHandler reply: @escaping @Sendable (Int, (any Error)?) -> Void)
```

```swift
func preallocateSpace(for item: FSItem, at offset: off_t, length: Int, flags: FSVolume.PreallocateFlags) async throws -> Int
```

```objc
- (void) preallocateSpaceForItem:(FSItem *) item atOffset:(off_t) offset length:(size_t) length flags:(FSPreallocateFlags) flags replyHandler:(void (^)(size_t bytesAllocated, NSError *error)) reply;
```

## Parameters

- `item`: The item for which to preallocate space.
- `offset`: The offset from which to allocate.
- `length`: The length of the space in bytes.
- `flags`: Flags that affect the preallocation behavior.
- `reply`: A block or closure to indicate success or failure. If preallocation succeeds, pass the amount of bytes allocated and a `nil` error. If preallocation fails, pass the relevant error as the second parameter; FSKit ignores any byte count in this case. For an `async` Swift implementation, there’s no reply handler; simply return the allocated byte count or throw an error.

## See Also

### Preallocating space
- [FSVolume.PreallocateFlags](../preallocateflags.md)
  Behavior flags for preallocation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateoperations/preallocatespace(for:at:length:flags:replyhandler:))*