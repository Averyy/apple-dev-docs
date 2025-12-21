# updateFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to update a fence after the acceleration structure pass completes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func updateFence(_ fence: any MTLFence)
```

#### Discussion

You can synchronize memory operations of an acceleration structure pass that access resources with an [`MTLFence`](mtlfence.md). This method instructs the pass to update `fence` after it runs all its memory store operations to the resources it accesses. The fence indicates when other passes can access those resources without a race condition.

For more information about synchronization with fences, see:

- [`Resource synchronization`](resource-synchronization.md)
- [`Synchronizing passes with a fence`](synchronizing-passes-with-a-fence.md)

##### Reuse a Fence By Waiting First and Updating Second

When encoding an acceleration structure pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [`waitForFence(_:)`](mtlaccelerationstructurecommandencoder/waitforfence(_:).md) method before encoding commands that need to wait for other passes.
2. Call the [`updateFence(_:)`](mtlaccelerationstructurecommandencoder/updatefence(_:).md) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ⚠️ **Warning**:  Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

## Parameters

- `fence`: A fence the pass updates after it completes.

## See Also

- [func waitForFence(any MTLFence)](mtlaccelerationstructurecommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to pause the acceleration structure pass until another pass updates a fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/updatefence(_:))*