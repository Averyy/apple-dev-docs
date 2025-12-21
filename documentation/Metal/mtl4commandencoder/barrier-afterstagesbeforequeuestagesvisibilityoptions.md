# barrier(afterStages:beforeQueueStages:visibilityOptions:)

**Framework**: Metal  
**Kind**: method

Encodes a producer barrier on work committed to the same command queue.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func barrier(afterStages: MTLStages, beforeQueueStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Mentions

- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md)
- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)

#### Discussion

This method encodes a barrier that guarantees that any work you encode using , corresponding to `beforeQueueStages`, don’t begin until all commands you previously encode in the current encoder (and prior encoders), corresponding to `afterStages`, complete.

When calling this method, you can pass any [`MTLStages`](mtlstages.md) to parameters `afterStages` and `beforeQueueStages`, even stages that don’t relate to the current or prior command encoders.

## Parameters

- `afterStages`:   mask that represents the stages of work to wait for.   This argument applies to work corresponding to these stages you encode in   the current command encoder prior to this barrier command.
- `beforeQueueStages`:   mask that represents the stages of work that need to wait.   This argument applies to subsequent encoders and not to work in the current   command encoder.
- `visibilityOptions`:   of the barrier, controlling cache flush behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:))*