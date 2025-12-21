# MTLFence

**Framework**: Metal  
**Kind**: protocol

A synchronization mechanism that orders memory operations between GPU passes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFence : NSObjectProtocol, Sendable
```

## Mentions

- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)
- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)

#### Overview

Create a fence by calling the [`makeFence()`](mtldevice/makefence().md) method.

A fence instructs the GPU to finish running specific stages of a pass before starting stages from another pass. This is useful when a pass needs to wait before loading data from a resource until after another pass stores data to that resource. For example, to synchronize two passes where one modifies a texture and another reads it, use a fence with the following steps:

1. Encode the producing pass and update a fence after the commands that modify the texture.
2. Encode the consuming pass and wait for the same fence before the commands that read from that texture.

Apple family GPUs can update and respond to fences on a per-stage basis. This means a GPU can delay running the commands for specific stages that need to wait for another pass while it runs other stages from the same pass. For example, a GPU can run the vertex stage of a pass while the fragment stage waits until another pass updates a fence. For more information about Apple family GPUs, see the [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) method, and the [`Metal feature set tables PDF`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) or the equivalent [`Metal feature set tables spreadsheet`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.zip).

The following encoder types support the [`updateFence(_:afterEncoderStages:)`](mtl4commandencoder/updatefence(_:afterencoderstages:).md) and [`waitForFence(_:beforeEncoderStages:)`](mtl4commandencoder/waitforfence(_:beforeencoderstages:).md) methods by conforming to the [`MTL4CommandEncoder`](mtl4commandencoder.md) protocol:

- [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md)
- [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md)
- [`MTL4MachineLearningCommandEncoder`](mtl4machinelearningcommandencoder.md)

The encoder types that inherit the [`MTLCommandEncoder`](mtlcommandencoder.md) protocol each have methods for updating and waiting for fences.

| Encoder types | Update fence methods | Wait for fence methods |
| --- | --- | --- |
| [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) | [`updateFence(_:after:)`](mtlrendercommandencoder/updatefence(_:after:).md) | [`waitForFence(_:before:)`](mtlrendercommandencoder/waitforfence(_:before:).md) |
| [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) | [`updateFence(_:)`](mtlcomputecommandencoder/updatefence(_:).md) | [`waitForFence(_:)`](mtlcomputecommandencoder/waitforfence(_:).md) |
| [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) | [`updateFence(_:)`](mtlblitcommandencoder/updatefence(_:).md) | [`waitForFence(_:)`](mtlblitcommandencoder/waitforfence(_:).md) |
| [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) | [`updateFence(_:)`](mtlaccelerationstructurecommandencoder/updatefence(_:).md) | [`waitForFence(_:)`](mtlaccelerationstructurecommandencoder/waitforfence(_:).md) |
| [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) | [`update(_:)`](mtlresourcestatecommandencoder/update(_:).md) | [`wait(for:)`](mtlresourcestatecommandencoder/wait(for:).md) |

> **Note**:  Earlier versions of Metal support hazard tracking for work you encode and commit with [`MTLCommandEncoder`](mtlcommandencoder.md), [`MTLCommandBuffer`](mtlcommandbuffer.md), and [`MTLCommandQueue`](mtlcommandqueue.md) instances, which means you don’t need to synchronize memory operations for resources with a [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property that’s equal to [`hazardTrackingModeTracked`](mtlresourceoptions/hazardtrackingmodetracked.md).

##### Submit Producing Passes Before Consuming Passes

Send producing passes that update a fence to a queue before submitting consuming passes that wait for a fence. When encoding the producing and consuming passes into the same command buffer, encode the producing passes before the consuming passes. When submitting the producing and consuming passes in different command buffers, commit the command buffers with the producing passes before those with the consuming passes.

> **Note**:  When submitting multiple command buffers to an [`MTL4CommandQueue`](mtl4commandqueue.md) at the same time, such as with its [`commit:count:options:`](mtl4commandqueue/commit:count:options:.md) method, the method commits the command buffers in array order.

Fences can synchronize passes you submit to different queues, including [`MTL4CommandQueue`](mtl4commandqueue.md), [`MTLCommandQueue`](mtlcommandqueue.md), or a combination of both.

> 💡 **Tip**:  Consider synchronizing passes that you submit to different queues with an [`MTLEvent`](mtlevent.md) instance instead.

## Topics

### Identifying a fence
- [var device: any MTLDevice](mtlfence/device.md)
  The device object that created the fence.
- [var label: String?](mtlfence/label.md)
  A string that identifies the fence.
### Selecting render stages
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)
  Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
  Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md)
  Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.
- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md)
  Block GPU stages in subsequent passes from running until stages in a pass, and earlier passes, finish.
- [Synchronizing CPU and GPU work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [struct MTLStages](mtlstages.md)
  The segments of command execution within the Metal pass types.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [struct MTL4VisibilityOptions](mtl4visibilityoptions.md)
  Memory consistency options for synchronization commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfence)*