# intermediatesHeapSize

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Obtain the size of the heap, in bytes, this pipeline requires during the execution.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var intermediatesHeapSize: Int { get }
```

#### Discussion

Use this value to allocate a [`MTLHeap`](mtlheap.md) instance of sufficient size that you can then provide to [`dispatchNetwork(intermediatesHeap:)`](mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:).md).

Metal uses this heap to store intermediate data as it executes the pipeline. It is your responsibility to provide a heap at least as large as this property requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinestate/intermediatesheapsize)*