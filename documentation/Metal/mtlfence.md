# MTLFence

**Framework**: Metal  
**Kind**: protocol

A memory fence to capture, track, and manage resource dependencies across command encoders.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFence : NSObjectProtocol
```

## Mentions

- [Tracking the Resource Residency of Argument Buffers](tracking-the-resource-residency-of-argument-buffers.md)

#### Overview

An [`MTLFence`](mtlfence.md) instance is typically used to track a resource created from an [`MTLHeap`](mtlheap.md) instance. You can also track non-heap resources that have tracking mode [`hazardTrackingModeUntracked`](mtlresourceoptions/hazardtrackingmodeuntracked.md).

To create an [`MTLFence`](mtlfence.md) instance, call the [`makeFence()`](mtldevice/makefence().md) method of an [`MTLDevice`](mtldevice.md) instance. A command encoder can either update a fence or wait for a fence.

> 💡 **Tip**:  When using a fence across multiple [`MTLCommandQueue`](mtlcommandqueue.md) instances, commit the queue that updates a fence before committing the queue that waits on a fence. Consider using an [`MTLEvent`](mtlevent.md) instead of a fence for these situations.

 When using a fence across multiple [`MTLCommandQueue`](mtlcommandqueue.md) instances, commit the queue that updates a fence before committing the queue that waits on a fence. Consider using an [`MTLEvent`](mtlevent.md) instead of a fence for these situations.

| Command encoders | Methods that update a fence | Methods that wait for a fence |
| --- | --- | --- |
| [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) | [`updateFence(_:)`](mtlblitcommandencoder/updatefence(_:).md) | [`waitForFence(_:)`](mtlblitcommandencoder/waitforfence(_:).md) |
| [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) | [`updateFence(_:)`](mtlcomputecommandencoder/updatefence(_:).md) | [`waitForFence(_:)`](mtlcomputecommandencoder/waitforfence(_:).md) |
| [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) | [`updateFence(_:after:)`](mtlrendercommandencoder/updatefence(_:after:).md) | [`waitForFence(_:before:)`](mtlrendercommandencoder/waitforfence(_:before:).md) |
| [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) | [`updateFence(_:)`](mtlaccelerationstructurecommandencoder/updatefence(_:).md) | [`waitForFence(_:)`](mtlaccelerationstructurecommandencoder/waitforfence(_:).md) |
| [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) | [`update(_:)`](mtlresourcestatecommandencoder/update(_:).md) | [`wait(for:)`](mtlresourcestatecommandencoder/wait(for:).md) |

## Topics

### Identifying the Fence
- [var device: any MTLDevice](mtlfence/device.md)
  The device object that created the fence.
- [var label: String?](mtlfence/label.md)
  A string that identifies the fence.
### Specifying Render Stages
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfence)*