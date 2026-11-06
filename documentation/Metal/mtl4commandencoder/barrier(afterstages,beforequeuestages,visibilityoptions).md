# barrier(afterStages:beforeQueueStages:visibilityOptions:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a producer barrier on work committed to the same command queue.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func barrier(afterStages: MTLStages, beforeQueueStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Mentions

- [Synchronizing passes with producer barriers](../synchronizing-passes-with-producer-barriers.md)
- [Synchronizing stages within a pass](../synchronizing-stages-within-a-pass.md)

## Discussion

This method encodes a barrier that guarantees that any work you encode using *subsequent command encoders*, corresponding to `beforeQueueStages`, don’t begin until all commands you previously encode in the current encoder (and prior encoders), corresponding to `afterStages`, complete.

When calling this method, you can pass any [`MTLStages`](../mtlstages.md) to parameters `afterStages` and `beforeQueueStages`, even stages that don’t relate to the current or prior command encoders.

## Barriers order work

A barrier orders work, not other barriers. Metal doesn’t guarantee that two barriers combine through a stage that they share, unless work in that stage runs between them and both barriers apply to that work. A fence update or a fence wait in that stage counts as work.

For example, `firstEncoder` and `secondEncoder` are consecutive encoders on the same command queue. The first barrier makes blit operations wait for dispatch operations, and the second barrier makes dispatch operations wait for blit operations. However, because no blit operations execute in `secondEncoder` before its barrier, Metal doesn’t guarantee that dispatch operations in encoders after `secondEncoder` wait for dispatch operations before the barrier in `firstEncoder`.

```swift
firstEncoder.barrier(afterStages: .dispatch,
               beforeQueueStages: .blit,
               visibilityOptions: [])
firstEncoder.endEncoding()

// Metal only synchronizes between these dispatch stages if you encode blit work

secondEncoder.barrier(afterStages: .blit,
                beforeQueueStages: .dispatch,
                visibilityOptions: [])
secondEncoder.endEncoding()
```

To make work in one stage wait for work in another stage, pass both stages to one barrier: the stage to wait for in `afterStages`, and the stage that waits in `beforeQueueStages`.

## Parameters

- `afterStages`: [`MTLStages`](../mtlstages.md) mask that represents the stages of work to wait for. This argument applies to work corresponding to these stages you encode in the current command encoder before this barrier command and in prior command encoders on the same command queue.
- `beforeQueueStages`: [`MTLStages`](../mtlstages.md) mask that represents the stages of work that need to wait. This argument applies to subsequent encoders and not to work in the current command encoder.
- `visibilityOptions`: [`MTL4VisibilityOptions`](../mtl4visibilityoptions.md) of the barrier, controlling cache flush behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:))*