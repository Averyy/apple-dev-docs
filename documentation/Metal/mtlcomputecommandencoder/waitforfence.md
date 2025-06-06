# waitForFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause pass execution until a fence updates.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence)
```

#### Discussion

Fences maintain command buffer order to prevent GPU data hazards as the GPU runs various passes. The GPU driver evaluates fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ❗ **Important**:  For a compute pass that updates and waits for the same fence, call [`waitForFence(_:)`](mtlcomputecommandencoder/waitforfence(_:).md) before you call [`updateFence(_:)`](mtlcomputecommandencoder/updatefence(_:).md). Updating a fence before waiting on it in the same encoder can cause a GPU deadlock.

 For a compute pass that updates and waits for the same fence, call [`waitForFence(_:)`](mtlcomputecommandencoder/waitforfence(_:).md) before you call [`updateFence(_:)`](mtlcomputecommandencoder/updatefence(_:).md). Updating a fence before waiting on it in the same encoder can cause a GPU deadlock.

On Apple family GPUs, [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instances place all fence update commands at the end of their pass.

## Parameters

- `fence`: An   instance to wait on.

## See Also

- [func updateFence(any MTLFence)](mtlcomputecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, allowing passes waiting on the fence to start or resume.
- [func memoryBarrier(scope: MTLBarrierScope)](mtlcomputecommandencoder/memorybarrier(scope:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [func memoryBarrier(resources: [any MTLResource])](mtlcomputecommandencoder/memorybarrier(resources:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/waitforfence(_:))*