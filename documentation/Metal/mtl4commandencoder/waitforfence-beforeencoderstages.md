# waitForFence(_:beforeEncoderStages:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to wait on a GPU fence.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func waitForFence(_ fence: any MTLFence, beforeEncoderStages: MTLStages)
```

## Mentions

- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)

#### Discussion

Encode a command that guarantees that any subsequent work you encode via this current command encoder, corresponding to `beforeEncoderStages`, doesn’t begin until all prior updates to the fence is complete.

To successfully wait for a fence update, schedule update and wait operations on the same command queue.

Use parameter `beforeEncoderStages` to pass in a combination of [`MTLStages`](mtlstages.md) for which this encoder can encode work. For example, for a [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) you can provide any combination of [`dispatch`](mtlstages/dispatch.md), [`blit`](mtlstages/blit.md) and [`accelerationStructure`](mtlstages/accelerationstructure.md).

## Parameters

- `fence`:   instance to wait for.
- `beforeEncoderStages`:   value that represents the stages of work that wait.   This argument only applies to work you encode in the current command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/waitforfence(_:beforeencoderstages:))*