# dispatchNetwork(intermediatesHeap:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Dispatches a machine learning network using the current pipeline state and argument table.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func dispatchNetwork(intermediatesHeap heap: any MTLHeap)
```

#### Discussion

This method takes a parameter consisting of a `MTLHeap` that Metal can use to allocate intermediate tensors. You can query the minimum size Metal requires for this heap by calling [`intermediatesHeapSize`](mtl4machinelearningpipelinestate/intermediatesheapsize.md).

## Parameters

- `heap`: A heap that Metal can use to allocate intermediate tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:))*