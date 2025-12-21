# barrier(afterQueueStages:beforeStages:visibilityOptions:)

**Framework**: Metal  
**Kind**: method

Encodes a consumer barrier on work you commit to the same command queue.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func barrier(afterQueueStages: MTLStages, beforeStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Mentions

- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md)
- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)

#### Discussion

Encode a barrier that guarantees that any subsequent work you encode in the current command encoder that corresponds to the `beforeStages` stages doesn’t proceed until Metal completes all work prior to the current command encoder corresponding to the `afterQueueStages` stages, completes.

Metal can reorder the exact point where it applies the barrier, so encode the barrier as close to the command that consumes the resource as possible. Don’t use this method for synchronizing resource access within the same pass.

If you need to synchronize work within a pass that you encode with an instance of a subclass of [`MTLCommandEncoder`](mtlcommandencoder.md), use memory barriers instead. For subclasses of [`MTL4CommandEncoder`](mtl4commandencoder.md), use encoder barriers.

You can specify `afterQueueStages` and `beforeStages` that contain [`MTLStages`](mtlstages.md) unrelated to the current command encoder.

## Parameters

- `afterQueueStages`:   mask that represents the stages of work to wait for.   This argument applies to work corresponding to these stages you   encode in prior command encoders, and not for the current encoder.
- `beforeStages`:   mask that represents the stages of work that wait.   This argument applies to work you encode in the current command encoder.
- `visibilityOptions`:   of the barrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:))*