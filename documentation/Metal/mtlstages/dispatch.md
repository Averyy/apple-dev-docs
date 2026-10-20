# dispatch

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

Represents all compute dispatches in a compute pass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var dispatch: MTLStages { get }
```

```c
MTLStageDispatch
```

## Mentions

- [Synchronizing passes with a fence](../synchronizing-passes-with-a-fence.md)
- [Synchronizing passes with consumer barriers](../synchronizing-passes-with-consumer-barriers.md)
- [Synchronizing passes with producer barriers](../synchronizing-passes-with-producer-barriers.md)
- [Synchronizing stages within a pass](../synchronizing-stages-within-a-pass.md)

## See Also

### Compute pass stages
- [static var blit: MTLStages](./blit.md)
  Represents all blit operations in a pass.
- [static var accelerationStructure: MTLStages](./accelerationstructure.md)
  Represents all acceleration structure operations.
- [static var machineLearning: MTLStages](./machinelearning.md)
  Represents all machine learning network dispatch operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstages/dispatch)*