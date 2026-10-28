# memoryBarrier(resources:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a memory barrier that enforces the order of write and read operations for specific resources.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS

## Declaration

```swift
func memoryBarrier(resources: [any MTLResource])
```

## Discussion

Memory barriers ensure the relevant passes finish updating resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## Parameters

- `resources`: An array of [`MTLResource`](../mtlresource.md) instances the barrier applies to.

## See Also

### Preventing resource access conflicts
- [func waitForFence(any MTLFence)](./waitforfence%28_%29.md)
  Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [func updateFence(any MTLFence)](./updatefence%28_%29.md)
  Encodes a command that instructs the GPU to update a fence after the compute pass completes.
- [func memoryBarrier(scope: MTLBarrierScope)](./memorybarrier%28scope%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/memorybarrier(resources:))*