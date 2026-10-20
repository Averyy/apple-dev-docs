# encode(to:sourceImages:sourceStates:intermediateImages:destinationStates:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?
```

```objc
- (MPSImage *) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(NSArray<MPSImage *> *) sourceImages sourceStates:(NSArray<MPSState *> *) sourceStates intermediateImages:(NSMutableArray<MPSImage *> *) intermediateImages destinationStates:(NSMutableArray<MPSState *> *) destinationStates;
```

## See Also

### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](./encode%28to,sourceimages%29.md)
- [class MPSState](../mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSNNBinaryGradientState](../mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [class MPSNNGradientState](../mpsnngradientstate.md)
  A class representing the state of a gradient kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](./executeasync%28withsourceimages,completionhandler%29.md)
- [typealias MPSNNGraphCompletionHandler](../mpsnngraphcompletionhandler.md)
  A notification when an asynchronous graph execution has finished.
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?](./encodebatch%28to,sourceimages,sourcestates%29.md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](./encodebatch%28to,sourceimages,sourcestates,intermediateimages,destinationstates%29.md)
- [func readCountForSourceImage(at: Int) -> Int](./readcountforsourceimage%28at%29.md)
- [func readCountForSourceState(at: Int) -> Int](./readcountforsourcestate%28at%29.md)
- [func reloadFromDataSources()](./reloadfromdatasources%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/encode(to:sourceimages:sourcestates:intermediateimages:destinationstates:))*