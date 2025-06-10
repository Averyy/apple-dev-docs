# size(ofCounterHeapEntry:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the size, in bytes, of each entry in a counter heap of a specific counter heap type when your app resolves it into a usable format.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func size(ofCounterHeapEntry type: MTL4CounterHeapType) -> Int
```

#### Return Value

The size of the post-transformation entry from a [`MTL4CounterHeap`](mtl4counterheap.md) of type [`MTL4CounterHeapType`](mtl4counterheaptype.md).

#### Discussion

In order to use the data available in a [`MTL4CounterHeap`](mtl4counterheap.md), your app first resolves it either in the CPU timeline or in the GPU timeline. When your app calls [`resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:`](mtl4commandbuffer/resolvecounterheap:withrange:intobuffer:atoffset:waitfence:updatefence:.md) to resolve counter data in the GPU timeline, Metal writes the data into a [`MTLBuffer`](mtlbuffer.md).

During this process, Metal transform the data in the heap into a format consisting of entries of the size that this method advertises, based on the [`MTL4CounterHeapType`](mtl4counterheaptype.md).

## Parameters

- `type`:   value that represents the type of the   to resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/size(ofcounterheapentry:))*