# waitForFence(_:before:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence, before stages: MTLRenderStages)
```

#### Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes, including render passes, within the same command queue. The render pass waits for a pass to update `fence` (see [`updateFence(_:after:)`](mtlrendercommandencoder/updatefence(_:after:).md)) before running any stage in the `stages` parameter.

> ❗ **Important**:  For a render pass that updates and waits for the same fence, call [`waitForFence(_:before:)`](mtlrendercommandencoder/waitforfence(_:before:).md) only before calling [`updateFence(_:after:)`](mtlrendercommandencoder/updatefence(_:after:).md). Updating a fence before waiting on it within the same encoder can cause GPU deadlock.

The GPU driver evaluates the pass’s fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

Apple family GPUs can update and respond to fences on a per-stage basis. That allows those GPUs to run portions of different stages, such as vertex and fragment, at the same time. You can check whether a GPU is in an Apple GPU family with the [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) method.

## Parameters

- `fence`: An   instance a pass updates to inform the GPU that it can begin running the applicable stages of the pass.
- `stages`: An   instance that designates which stages in the render pass apply to  .

## See Also

- [func updateFence(any MTLFence, after: MTLRenderStages)](mtlrendercommandencoder/updatefence(_:after:).md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which signals passes waiting on the fence.
- [func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(resources:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(scope:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/waitforfence(_:before:))*