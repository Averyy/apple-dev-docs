# intermediatesHeapSize

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Obtain the size of the heap, in bytes, this pipeline requires during the execution.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var intermediatesHeapSize: Int { get }
```

#### Discussion

Use this value to allocate a [`MTLHeap`](mtlheap.md) instance of sufficient size that you can then provide to [`dispatchNetwork(intermediatesHeap:)`](mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:).md).

Metal uses this heap to store intermediate data as it executes the pipeline. It is your responsibility to provide a heap at least as large as this property requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinestate/intermediatesheapsize)*