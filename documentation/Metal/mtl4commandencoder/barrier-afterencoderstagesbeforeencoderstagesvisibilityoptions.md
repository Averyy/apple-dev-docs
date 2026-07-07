# barrier(afterEncoderStages:beforeEncoderStages:visibilityOptions:)

**Framework**: Metal  
**Kind**: method

Encodes an intra-pass barrier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func barrier(afterEncoderStages: MTLStages, beforeEncoderStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Mentions

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)

#### Discussion

Encode a barrier that guarantees that any subsequent work you encode in the *current command encoder*, corresponding to `beforeEncoderStages`, doesn’t begin until all prior commands in this command encoder, corresponding to `afterEncoderStages`, completes.

When calling this method, it’s your responsibility to ensure parameters `afterEncoderStages` and `beforeEncoderStages` contain a combination of [`MTLStages`](mtlstages.md) for which this encoder can encode commands. For example, for a [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) instance, you can provide any combination of [`dispatch`](mtlstages/dispatch.md), [`blit`](mtlstages/blit.md) and [`accelerationStructure`](mtlstages/accelerationstructure.md).

## Parameters

- `afterEncoderStages`: [`MTLStages`](mtlstages.md) mask that represents the stages of work to wait for. This argument only applies to subsequent work you encode in the current command encoder.
- `beforeEncoderStages`: [`MTLStages`](mtlstages.md) mask that represents the stages of work that wait. This argument only applies to work you encode in the current command encoder prior to this barrier.
- `visibilityOptions`: [`MTL4VisibilityOptions`](mtl4visibilityoptions.md) of the barrier, controlling cache flush behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterencoderstages:beforeencoderstages:visibilityoptions:))*