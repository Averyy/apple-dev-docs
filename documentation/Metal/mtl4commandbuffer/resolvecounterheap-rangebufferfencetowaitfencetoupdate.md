# resolveCounterHeap(_:range:buffer:fenceToWait:fenceToUpdate:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resolves an opaque counter heap into a buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func resolveCounterHeap(_ counterHeap: any MTL4CounterHeap, range: Range<Int>, buffer: MTL4BufferRange, fenceToWait: (any MTLFence)? = nil, fenceToUpdate: (any MTLFence)? = nil)
```

#### Discussion

The command converts the data within a counter heap into a common format and stores it in `buffer`.

The command places each entry in the counter heap within `range` sequentially. Each entry has a fixed size that you can query by calling the [`size(ofCounterHeapEntry:)`](mtldevice/size(ofcounterheapentry:).md) method.

This command runs during the blit stage of the GPU timeline. Barrier against this stage to ensure the data is present in the buffer before you access it.

> **Note**: Your app needs to ensure the GPU places data in the heap before you resolve it by synchronizing this stage with other GPU operations.

Similarly, your app needs to synchronize any GPU accesses to `buffer` after the command completes with a barrier.

If your app needs to access `buffer` from the CPU, signal an [`MTLSharedEvent`](mtlsharedevent.md) to notify the CPU when it’s ready. Alternatively, you can resolve the heap’s data from the CPU by calling the heap’s [`resolveCounterRange:`](mtl4counterheap/resolvecounterrange:.md) method.

## Parameters

- `counterHeap`: A counter heap the command resolves.
- `range`: A range of index values within the heap to resolve.
- `buffer`: A buffer where the command stores the resolved data.
- `fenceToWait`: An optional fence the GPU waits for before starting; otherwise `nil`.
- `fenceToUpdate`: An optional fence the system updates after the command finishes resolving the data; otherwise `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/resolvecounterheap(_:range:buffer:fencetowait:fencetoupdate:))*