# dispatchNetwork(intermediatesHeap:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Dispatches a machine learning network using the current pipeline state and argument table.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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