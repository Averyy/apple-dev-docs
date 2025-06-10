# updateFence(_:afterEncoderStages:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to update a GPU fence.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func updateFence(_ fence: any MTLFence, afterEncoderStages: MTLStages)
```

## Mentions

- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)

#### Discussion

This method encodes a command that updates a [`MTLFence`](mtlfence.md) instance after all previously-encoded commands in the current command encoder, corresponding to `afterEncoderStages`, complete.

Use parameter `afterEncoderStages` to pass in a combination of [`MTLStages`](mtlstages.md) for which this encoder can encode work. For example, for a [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) you can provide any combination of [`dispatch`](mtlstages/dispatch.md), [`blit`](mtlstages/blit.md) and [`accelerationStructure`](mtlstages/accelerationstructure.md).

## Parameters

- `fence`:   instance to update.
- `afterEncoderStages`:   value that represents the stages of work to wait for.   This argument only applies to work encoded in the current command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/updatefence(_:afterencoderstages:))*