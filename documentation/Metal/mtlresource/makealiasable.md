# makeAliasable()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Allows future heap resource allocations to alias against the resource’s memory, reusing it.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeAliasable()
```

#### Discussion

> ❗ **Important**:  This method is only valid for heap-allocated resources using the [`MTLHeapType.automatic`](mtlheaptype/automatic.md) allocator.

 This method is only valid for heap-allocated resources using the [`MTLHeapType.automatic`](mtlheaptype/automatic.md) allocator.

Resource instances marked as aliased have backing memory available for use in new allocations to the heap. One common use case is to make a single large resource aliasable for reuse of memory by smaller and more frequent resource allocations. For situations where you need fine-grained control over your memory management, you might want to use a heap with the allocation type [`MTLHeapType.placement`](mtlheaptype/placement.md) and manage memory yourself instead.

Aliased resources can’t be un-aliased or moved. If you use an aliased resource instance to read or write data, it results in undefined behavior.

> ⚠️ **Warning**:  When you alias a resource, make sure it’s safe to release the underlying data. Accessing the data of an aliased resource instance can cause memory corruption.

 When you alias a resource, make sure it’s safe to release the underlying data. Accessing the data of an aliased resource instance can cause memory corruption.

When working with resources possibly backed by aliased memory, you should take great care that the system doesn’t access resources from multiple aliases concurrently. Use an [`MTLEvent`](mtlevent.md) or [`MTLFence`](mtlfence.md) instance to protect access to resources that you’ve either already aliased or intend to alias.

The general process to reuse memory from aliased resources is:

1. Allocate an [`MTLHeap`](mtlheap.md) instance to hold your task’s resources, using the [`makeHeap(descriptor:)`](mtldevice/makeheap(descriptor:).md) method. Your heap should be big enough to store the maximum amount of concurrently loaded data you expect.
2. Allocate your resource(s) using a heap method that returns an [`MTLResource`](mtlresource.md) instance.
3. Perform your stage on the GPU, and when it completes, mark the resource allocation(s) as aliasable by calling this method.
4. For each successive stage of your overall pass, repeat steps 2 and 3. Ensure that the prior stage fully completes before making any new resources on an aliasable heap through an event or fence.

## See Also

- [var heapOffset: Int](mtlresource/heapoffset.md)
  The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [var heap: (any MTLHeap)?](mtlresource/heap.md)
  The heap on which the resource is allocated, if any.
- [func isAliasable() -> Bool](mtlresource/isaliasable.md)
  A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/makealiasable())*