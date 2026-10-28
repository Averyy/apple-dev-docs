# resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that resolves an opaque counter heap into a buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) resolveCounterHeap:(id<MTL4CounterHeap>) counterHeap withRange:(NSRange) range intoBuffer:(MTL4BufferRange) bufferRange waitFence:(id<MTLFence>) fenceToWait updateFence:(id<MTLFence>) fenceToUpdate;
```

## Discussion

The command this method encodes converts the data within `counterHeap` into a common format and stores it into the `bufferRange` parameter.

The command places each entry in the counter heap within `range` sequentially, starting at `alignedOffset`. Each entry needs to be a fixed size that you can query by calling the [`size(ofCounterHeapEntry:)`](../mtldevice/size%28ofcounterheapentry%29.md) method.

This command runs during the `MTLStageBlit` stage of the GPU timeline. Barrier against this stage to ensure the data is present in the resolve buffer parameter before you access it.

> **Note**: Your app needs ensure the GPU places data in the heap before you resolve it by synchronizing this stage with other GPU operations.

Similarly, your app needs to synchronize any GPU accesses to `bufferRange` after the command completes with barrier.

If your app needs to access `bufferRange` from the CPU, signal an [`MTLSharedEvent`](../mtlsharedevent.md) to notify the CPU when it’s ready. Alternatively, you can resolve the heap’s data from the CPU by calling the heap’s [`resolveCounterRange:`](../mtl4counterheap/resolvecounterrange_.md) method.

## Parameters

- `counterHeap`: A heap the command resolves.
- `range`: A range of index values within the heap the command resolves.
- `bufferRange`: The buffer the command saves the data it resolves into.
- `fenceToWait`: A fence the GPU waits for before starting, if applicable; otherwise `nil`.
- `fenceToUpdate`: A fence the system updates after the command finishes resolving the data; otherwise `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/resolvecounterheap:withrange:intobuffer:waitfence:updatefence:)*