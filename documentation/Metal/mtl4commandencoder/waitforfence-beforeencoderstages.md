# waitForFence(_:beforeEncoderStages:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause before starting one or more stages of the pass until a pass updates a fence.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence, beforeEncoderStages: MTLStages)
```

## Mentions

- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)

#### Discussion

You can synchronize memory operations of a pass that access resources with an [`MTLFence`](mtlfence.md). This method instructs the GPU to wait until another pass updates `fence` before running the stages you pass to the `beforeEncoderStages` parameter. The fence indicates when the pass can access those resources without a race condition.

For more information about synchronization with fences, see:

- [`Resource synchronization`](resource-synchronization.md)
- [`Synchronizing passes with a fence`](synchronizing-passes-with-a-fence.md)

##### Reuse a Fence By Waiting First and Updating Second

When encoding a pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [`waitForFence(_:beforeEncoderStages:)`](mtl4commandencoder/waitforfence(_:beforeencoderstages:).md) method before encoding commands that need to wait for other passes.
2. Call the [`updateFence(_:afterEncoderStages:)`](mtl4commandencoder/updatefence(_:afterencoderstages:).md) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ⚠️ **Warning**:  Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

To synchronize different stages within a single pass, create an  because a fence can only synchronize memory operations between different passes. For more information, see [`Synchronizing stages within a pass`](synchronizing-stages-within-a-pass.md).

## Parameters

- `fence`: A fence that the pass waits for before running the stages you pass to  .
- `beforeEncoderStages`: The encoder stages that need to wait for another pass to update   before they run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/waitforfence(_:beforeencoderstages:))*