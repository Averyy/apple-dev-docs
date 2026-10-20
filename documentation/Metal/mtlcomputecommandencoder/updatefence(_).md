# updateFence(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that instructs the GPU to update a fence after the compute pass completes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func updateFence(_ fence: any MTLFence)
```

```objc
- (void) updateFence:(id<MTLFence>) fence;
```

#### Discussion

You can synchronize memory operations of a compute pass that access resources with an [`MTLFence`](../mtlfence.md). This method instructs the pass to update `fence` after it runs all its memory store operations to the resources it accesses. The fence indicates when other passes can access those resources without a race condition.

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

- `fence`: A fence the pass updates after it completes.

## See Also

### Preventing resource access conflicts
- [func waitForFence(any MTLFence)](./waitforfence%28_%29.md)
  Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [func memoryBarrier(scope: MTLBarrierScope)](./memorybarrier%28scope%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [func memoryBarrier(resources: [any MTLResource])](./memorybarrier%28resources%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/updatefence(_:))*