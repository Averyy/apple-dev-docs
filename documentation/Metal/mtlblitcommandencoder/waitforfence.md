# waitForFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause the blit pass until another pass updates a fence.

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

You can synchronize memory operations of a blit pass that access resources with an [`MTLFence`](mtlfence.md). This method instructs the GPU to wait until another pass updates `fence` before running the blit pass. The fence indicates when the pass can access those resources without a race condition.

For more information about synchronization with fences, see:

- [`Resource synchronization`](resource-synchronization.md)
- [`Synchronizing passes with a fence`](synchronizing-passes-with-a-fence.md)

##### Reuse a Fence By Waiting First and Updating Second

When encoding a blit pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [`waitForFence(_:)`](mtlblitcommandencoder/waitforfence(_:).md) method before encoding commands that need to wait for other passes.
2. Call the [`updateFence(_:)`](mtlblitcommandencoder/updatefence(_:).md) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ⚠️ **Warning**:  Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

## Parameters

- `fence`: A fence that the pass waits for before it runs any of its commands.

## See Also

- [func updateFence(any MTLFence)](mtlblitcommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence after the blit pass completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/waitforfence(_:))*