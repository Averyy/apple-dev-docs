# waitForFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause the acceleration structure pass until another pass updates a fence.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence)
```

#### Discussion

You can synchronize memory operations of an acceleration structure pass that access resources with an [`MTLFence`](mtlfence.md). This method instructs the GPU to wait until another pass updates `fence` before running the acceleration structure pass. The fence indicates when the pass can access those resources without a race condition.

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

- `fence`: A fence that the pass waits for before it runs any of its commands.

## See Also

- [func updateFence(any MTLFence)](mtlaccelerationstructurecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence after the acceleration structure pass completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/waitforfence(_:))*