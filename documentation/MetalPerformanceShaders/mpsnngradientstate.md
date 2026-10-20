# MPSNNGradientState

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A class representing the state of a gradient kernel when it was encoded.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNGradientState
```

```objc
@interface MPSNNGradientState : MPSState
```

## Relationships

### Inherits From
- [MPSState](./mpsstate.md)
### Inherited By
- [MPSCNNBatchNormalizationState](./mpscnnbatchnormalizationstate.md)
- [MPSCNNConvolutionGradientState](./mpscnnconvolutiongradientstate.md)
- [MPSCNNDropoutGradientState](./mpscnndropoutgradientstate.md)
- [MPSCNNGroupNormalizationGradientState](./mpscnngroupnormalizationgradientstate.md)
- [MPSCNNInstanceNormalizationGradientState](./mpscnninstancenormalizationgradientstate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](./mpsnngraph/encode%28to,sourceimages%29.md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](./mpsnngraph/encode%28to,sourceimages,sourcestates,intermediateimages,destinationstates%29.md)
- [class MPSState](./mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSNNBinaryGradientState](./mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](./mpsnngraph/executeasync%28withsourceimages,completionhandler%29.md)
- [typealias MPSNNGraphCompletionHandler](./mpsnngraphcompletionhandler.md)
  A notification when an asynchronous graph execution has finished.
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?](./mpsnngraph/encodebatch%28to,sourceimages,sourcestates%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](./mpsnngraph/encodebatch%28to,sourceimages,sourcestates,intermediateimages,destinationstates%29.md)
- [func readCountForSourceImage(at: Int) -> Int](./mpsnngraph/readcountforsourceimage%28at%29.md)
- [func readCountForSourceState(at: Int) -> Int](./mpsnngraph/readcountforsourcestate%28at%29.md)
- [func reloadFromDataSources()](./mpsnngraph/reloadfromdatasources%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngradientstate)*