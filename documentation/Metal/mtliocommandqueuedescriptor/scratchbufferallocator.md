# scratchBufferAllocator

**Framework**: Metal  
**Kind**: property

An optional memory allocator that you implement to manage the scratch memory that an input/output command queue requests.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var scratchBufferAllocator: (any MTLIOScratchBufferAllocator)? { get set }
```

#### Discussion

Your app can manage an input/output command queue’s scratch memory by an implementing [`MTLIOScratchBufferAllocator`](mtlioscratchbufferallocator.md) in one of your types, and assigning an instance of it to [`scratchBufferAllocator`](mtliocommandqueuedescriptor/scratchbufferallocator.md). Otherwise, set to `nil` to instruct the input/output command queue to allocate and manage its own scratch buffers.

> **Note**:  An input/output command queue uses scratch buffers for memory-intensives tasks, including loading textures and decompressing asset files.

 An input/output command queue uses scratch buffers for memory-intensives tasks, including loading textures and decompressing asset files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/scratchbufferallocator)*