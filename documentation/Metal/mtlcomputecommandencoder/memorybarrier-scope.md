# memoryBarrier(scope:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a memory barrier that enforces the order of write and read operations for specific resource types.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func memoryBarrier(scope: MTLBarrierScope)
```

#### Discussion

Memory barriers ensure the relevant passes finish updating resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## Parameters

- `scope`: An   instance that represents the resource types the barrier synchronizes operations on.

## See Also

- [func waitForFence(any MTLFence)](mtlcomputecommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to pause pass execution until a fence updates.
- [func updateFence(any MTLFence)](mtlcomputecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, allowing passes waiting on the fence to start or resume.
- [func memoryBarrier(resources: [any MTLResource])](mtlcomputecommandencoder/memorybarrier(resources:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/memorybarrier(scope:))*