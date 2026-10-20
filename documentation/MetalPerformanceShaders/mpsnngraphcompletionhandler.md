# MPSNNGraphCompletionHandler

**Framework**: Metal Performance Shaders  
**Kind**: typealias  
**Role**: Type Alias

A notification when an asynchronous graph execution has finished.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MPSNNGraphCompletionHandler = (MPSImage?, (any Error)?) -> Void
```

```c
typedef void (^)(MPSImage *, NSError *) MPSNNGraphCompletionHandler;
```

## See Also

### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](./mpsnngraph/encode%28to,sourceimages%29.md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](./mpsnngraph/encode%28to,sourceimages,sourcestates,intermediateimages,destinationstates%29.md)
- [class MPSState](./mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSNNBinaryGradientState](./mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [class MPSNNGradientState](./mpsnngradientstate.md)
  A class representing the state of a gradient kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](./mpsnngraph/executeasync%28withsourceimages,completionhandler%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?](./mpsnngraph/encodebatch%28to,sourceimages,sourcestates%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](./mpsnngraph/encodebatch%28to,sourceimages,sourcestates,intermediateimages,destinationstates%29.md)
- [func readCountForSourceImage(at: Int) -> Int](./mpsnngraph/readcountforsourceimage%28at%29.md)
- [func readCountForSourceState(at: Int) -> Int](./mpsnngraph/readcountforsourcestate%28at%29.md)
- [func reloadFromDataSources()](./mpsnngraph/reloadfromdatasources%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraphcompletionhandler)*