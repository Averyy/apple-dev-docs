# barrier(afterQueueStages:beforeStages:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a consumer barrier on work you commit to the same command queue.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func barrier(afterQueueStages: MTLStages, beforeStages: MTLStages)
```

#### Discussion

Encode a barrier that guarantees that any subsequent work you encode in the current command encoder that corresponds to the `beforeStages` stages doesn’t proceed until Metal completes all work prior to the current command encoder corresponding to the `afterQueueStages` stages, completes.

Metal can reorder the exact point where it applies the barrier, so use this method for synchronizing between different passes.

If you need to synchronize work within a pass that you encode with an instance of a subclass of [`MTLCommandEncoder`](mtlcommandencoder.md), use memory barriers instead. For subclasses of [`MTL4CommandEncoder`](mtl4commandencoder.md), use encoder barriers.

You can specify `afterQueueStages` and `beforeStages` that contain [`MTLStages`](mtlstages.md) unrelated to the current command encoder.

## Parameters

- `afterQueueStages`:   mask that represents the stages of work to wait for.   This argument applies to work corresponding to these stages you   encode in prior command encoders, and not for the current encoder.
- `beforeStages`:   mask that represents the stages of work that wait.   This argument applies to work you encode in the current command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/barrier(afterqueuestages:beforestages:))*