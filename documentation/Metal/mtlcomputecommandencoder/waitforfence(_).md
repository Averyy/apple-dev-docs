# waitForFence(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.

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

```objc
- (void) waitForFence:(id<MTLFence>) fence;
```

#### Discussion

You can synchronize memory operations of a compute pass that access resources with an [`MTLFence`](../mtlfence.md). This method instructs the GPU to wait until another pass updates `fence` before running the compute pass. The fence indicates when the pass can access those resources without a race condition.

For more information about synchronization with fences, see:

- [Resource synchronization](../resource-synchronization.md)
- [Synchronizing passes with a fence](../synchronizing-passes-with-a-fence.md)

##### Reuse a fence by waiting first and updating second

When encoding a compute pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [`waitForFence(_:)`](./waitforfence%28_%29.md) method before encoding commands that need to wait for other passes.
2. Call the [`updateFence(_:)`](./updatefence%28_%29.md) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [`MTLCommandBuffer`](../mtlcommandbuffer.md).

> ⚠️ **Warning**:  Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

## Parameters

- `fence`: A fence that the pass waits for before it runs any of its commands.

## See Also

### Preventing resource access conflicts
- [func updateFence(any MTLFence)](./updatefence%28_%29.md)
  Encodes a command that instructs the GPU to update a fence after the compute pass completes.
- [func memoryBarrier(scope: MTLBarrierScope)](./memorybarrier%28scope%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [func memoryBarrier(resources: [any MTLResource])](./memorybarrier%28resources%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [- memoryBarrierWithResources:count:](./memorybarrierwithresources_count_.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/waitforfence(_:))*