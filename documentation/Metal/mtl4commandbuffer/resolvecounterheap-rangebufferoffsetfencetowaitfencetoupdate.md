# resolveCounterHeap(_:range:buffer:offset:fenceToWait:fenceToUpdate:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resolves an opaque counter heap into a buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func resolveCounterHeap(_ counterHeap: any MTL4CounterHeap, range: Range<Int>, buffer: any MTLBuffer, offset: Int, fenceToWait: (any MTLFence)? = nil, fenceToUpdate: (any MTLFence)? = nil)
```

#### Discussion

The command this method encodes converts the data within a counter heap into a common format and stores it into the `buffer` parameter.

The command places each entry in the counter heap within `range` sequentially, starting at `offset`. Each entry needs to be a fixed size that you can query by calling the [`size(ofCounterHeapEntry:)`](mtldevice/size(ofcounterheapentry:).md) method.

This command runs during the `MTLStageBlit` stage of the GPU timeline. Barrier against this stage to ensure the data is present in the resolve buffer parameter before you access it.

> **Note**: Your app needs ensure the GPU places data in the heap before you resolve it by synchronizing this stage with other GPU operations.

Similarly, your app needs to synchronize any GPU accesses to `buffer` after the command completes with barrier.

If your app needs to access `buffer` from the CPU, signal an [`MTLSharedEvent`](mtlsharedevent.md) to notify the CPU when it’s ready. Alternatively, you can resolve the heap’s data from the CPU by calling the heap’s [`resolveCounterRange(_:)`](mtl4counterheap/resolvecounterrange(_:)-49tmw.md) method.

## Parameters

- `counterHeap`: A heap the command resolves.
- `range`: A range of index values within the heap the command resolves.
- `buffer`: A buffer the command saves the data it resolves into.
- `offset`: An offset within   that indicates where the command begins writing the data.
- `fenceToWait`: A fence the GPU waits for before starting, if applicable; otherwise  .
- `fenceToUpdate`: A fence the system updates after the command finishes resolving the data; otherwise  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/resolvecounterheap(_:range:buffer:offset:fencetowait:fencetoupdate:))*