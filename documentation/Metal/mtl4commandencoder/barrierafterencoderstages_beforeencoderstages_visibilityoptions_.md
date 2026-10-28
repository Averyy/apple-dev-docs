# barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes an intra-pass barrier that instructs the GPU to pause before running stages of subsequent commands until stages of previous commands complete.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) barrierAfterEncoderStages:(MTLStages) afterEncoderStages beforeEncoderStages:(MTLStages) beforeEncoderStages visibilityOptions:(MTL4VisibilityOptions) visibilityOptions;
```

## Discussion

Encode a barrier that guarantees that any subsequent work you encode in the *current command encoder*, corresponding to `beforeEncoderStages`, doesn’t begin until all prior commands in this command encoder, corresponding to `afterEncoderStages`, completes.

When calling this method, it’s your responsibility to ensure parameters `afterEncoderStages` and `beforeEncoderStages` contain a combination of [`MTLStages`](../mtlstages.md) for which this encoder can encode commands. For example, for a [`MTL4ComputeCommandEncoder`](../mtl4computecommandencoder.md) instance, you can provide any combination of [`dispatch`](../mtlstages/dispatch.md), [`blit`](../mtlstages/blit.md) and [`accelerationStructure`](../mtlstages/accelerationstructure.md).

## Parameters

- `afterEncoderStages`: [`MTLStages`](../mtlstages.md) the stages of the previous commands of this pass that need to complete before the stages in `beforeEncoderStages` start for subsequent commands you encode in this pass.
- `beforeEncoderStages`: [`MTLStages`](../mtlstages.md) the stages of the subsequent commands you encode in this pass that wait for the stages in `afterEncoderStages`, within this pass, to complete.
- `visibilityOptions`: [`MTL4VisibilityOptions`](../mtl4visibilityoptions.md) of the barrier, controlling cache flush behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/barrierafterencoderstages:beforeencoderstages:visibilityoptions:)*