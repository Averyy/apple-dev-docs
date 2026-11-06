# barrier(afterQueueStages:beforeStages:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a consumer barrier on work you commit to the same command queue.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func barrier(afterQueueStages: MTLStages, beforeStages: MTLStages)
```

```objc
- (void) barrierAfterQueueStages:(MTLStages) afterQueueStages beforeStages:(MTLStages) beforeStages;
```

## Discussion

Encode a barrier that guarantees that any subsequent work you encode in the current command encoder, and future command encoders on the same command queue, that corresponds to the `beforeStages` stages doesn’t proceed until Metal completes all work prior to the current command encoder corresponding to the `afterQueueStages` stages.

Metal can reorder the exact point where it applies the barrier, so use this method for synchronizing between different passes.

If you need to synchronize work within a pass that you encode with an instance of a subclass of [`MTLCommandEncoder`](../mtlcommandencoder.md), use memory barriers instead. For subclasses of [`MTL4CommandEncoder`](../mtl4commandencoder.md), use encoder barriers.

You can specify `afterQueueStages` and `beforeStages` that contain [`MTLStages`](../mtlstages.md) unrelated to the current command encoder.

## Barriers order work

A barrier orders work, not other barriers. Metal doesn’t guarantee that two barriers combine through a stage that they share, unless work in that stage runs between them and both barriers apply to that work.

For example, `firstEncoder` and `secondEncoder` are consecutive encoders on the same command queue. The first barrier makes blit operations wait for dispatch operations, and the second barrier makes dispatch operations wait for blit operations. However, because no blit operations execute in `firstEncoder` after its barrier, Metal doesn’t guarantee that dispatch operations after the barrier in `secondEncoder`, and in later encoders, wait for dispatch operations in encoders before `firstEncoder`.

**Swift**:

```swift
firstEncoder.barrier(afterQueueStages: .dispatch,
                     beforeStages: .blit)
firstEncoder.endEncoding()

// Metal only synchronizes between these dispatch stages if you encode blit work

secondEncoder.barrier(afterQueueStages: .blit,
                      beforeStages: .dispatch)
secondEncoder.endEncoding()
```

**Objective-C**:

```obj-c
[firstEncoder barrierAfterQueueStages:MTLStageDispatch
                         beforeStages:MTLStageBlit];
[firstEncoder endEncoding];

// Metal only synchronizes between these dispatch stages if you encode blit work

[secondEncoder barrierAfterQueueStages:MTLStageBlit
                          beforeStages:MTLStageDispatch];
[secondEncoder endEncoding];
```

**C++**:

```cpp
firstEncoder->barrierAfterQueueStages(MTL::StageDispatch,
                                      MTL::StageBlit);
firstEncoder->endEncoding();

// Metal only synchronizes between these dispatch stages if you encode blit work

secondEncoder->barrierAfterQueueStages(MTL::StageBlit,
                                       MTL::StageDispatch);
secondEncoder->endEncoding();
```

To make work in one stage wait for work in another stage, pass both stages to one barrier: the stage to wait for in `afterQueueStages`, and the stage that waits in `beforeStages`.

## Parameters

- `afterQueueStages`: [`MTLStages`](../mtlstages.md) mask that represents the stages of work to wait for. This argument applies to work corresponding to these stages you encode in prior command encoders, and not for the current encoder.
- `beforeStages`: [`MTLStages`](../mtlstages.md) mask that represents the stages of work that wait. This argument applies to work you encode in the current command encoder and future command encoders on the same command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/barrier(afterqueuestages:beforestages:))*