# MPSNNGraphCompletionHandler

**Framework**: Metal Performance Shaders  
**Kind**: typealias

A notification when an asynchronous graph execution has finished.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MPSNNGraphCompletionHandler = (MPSImage?, (any Error)?) -> Void
```

## See Also

- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](mpsnngraph/encode(to:sourceimages:).md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](mpsnngraph/encode(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [class MPSState](mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSNNBinaryGradientState](mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [class MPSNNGradientState](mpsnngradientstate.md)
  A class representing the state of a gradient kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](mpsnngraph/executeasync(withsourceimages:completionhandler:).md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:).md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [func readCountForSourceImage(at: Int) -> Int](mpsnngraph/readcountforsourceimage(at:).md)
- [func readCountForSourceState(at: Int) -> Int](mpsnngraph/readcountforsourcestate(at:).md)
- [func reloadFromDataSources()](mpsnngraph/reloadfromdatasources.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraphcompletionhandler)*