# memoryBarrier(resources:)

**Framework**: Metal  
**Kind**: method

Creates a memory barrier that enforces the order of write and read operations for specific resources.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+

## Declaration

```swift
func memoryBarrier(resources: [any MTLResource])
```

#### Discussion

Memory barriers ensure the relevant passes finish updating resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## Parameters

- `resources`: An array of   instances the barrier applies to.

## See Also

- [func waitForFence(any MTLFence)](mtlcomputecommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [func updateFence(any MTLFence)](mtlcomputecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence after the compute pass completes.
- [func memoryBarrier(scope: MTLBarrierScope)](mtlcomputecommandencoder/memorybarrier(scope:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/memorybarrier(resources:))*