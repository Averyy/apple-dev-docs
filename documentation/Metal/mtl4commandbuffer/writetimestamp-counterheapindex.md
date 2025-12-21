# writeTimestamp(counterHeap:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Writes a GPU timestamp into the given counter heap.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func writeTimestamp(counterHeap: any MTL4CounterHeap, index: Int)
```

#### Discussion

This method captures a timestamp after work prior to this command in the command buffer is complete. Work after this call may or may not have started.

You are responsible for ensuring the `counterHeap` is of type [`MTL4CounterHeapType.timestamp`](mtl4counterheaptype/timestamp.md).

## Parameters

- `counterHeap`:   to write the timestamp into.
- `index`: The index within the   that Metal writes the timestamp to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/writetimestamp(counterheap:index:))*