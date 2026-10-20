# paddingPolicy

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var paddingPolicy: any MPSNNPadding { get set }
```

```objc
@property (nonatomic, retain, readwrite, nonnull) id<MPSNNPadding> paddingPolicy;
```

## See Also

### Instance Properties
- [var label: String?](./label.md)
- [protocol MPSNNPadding](../mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var resultImage: MPSNNImageNode](./resultimage.md)
- [var resultState: MPSNNStateNode?](./resultstate.md)
- [var resultStates: [MPSNNStateNode]?](./resultstates.md)
- [class MPSNNStateNode](../mpsnnstatenode.md)
  A placeholder node denoting the position in the graph of a state object.
- [class MPSNNBinaryGradientStateNode](../mpsnnbinarygradientstatenode.md)
  A representation of the state created to record the properties of a binary gradient kernel.
- [class MPSNNGradientStateNode](../mpsnngradientstatenode.md)
  A representation of the state created to record the properties of a gradient kernel at the time it was encoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnfilternode/paddingpolicy)*