# readCountForSourceState(at:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.0+
- macOS 10.14.1+
- tvOS 12.1+
- visionOS 1.0+

## Declaration

```swift
func readCountForSourceState(at index: Int) -> Int
```

```objc
- (NSUInteger) readCountForSourceStateAtIndex:(NSUInteger) index;
```

## See Also

### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](./encode%28to,sourceimages%29.md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](./encode%28to,sourceimages,sourcestates,intermediateimages,destinationstates%29.md)
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
- [func reloadFromDataSources()](./reloadfromdatasources%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/readcountforsourcestate(at:))*