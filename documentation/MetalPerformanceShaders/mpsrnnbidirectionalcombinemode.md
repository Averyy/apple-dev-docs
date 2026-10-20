# MPSRNNBidirectionalCombineMode

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

Modes that define how two images or matrices are combined.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MPSRNNBidirectionalCombineMode
```

```c
enum MPSRNNBidirectionalCombineMode : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSRNNBidirectionalCombineMode.add](./mpsrnnbidirectionalcombinemode/add.md)
  A mode in which two sequences are summed to form a single output.
- [MPSRNNBidirectionalCombineMode.concatenate](./mpsrnnbidirectionalcombinemode/concatenate.md)
  A mode in which two sequences are concatenated along the feature channels to form a single output.
- [MPSRNNBidirectionalCombineMode.none](./mpsrnnbidirectionalcombinemode/none.md)
  A mode in which two sequences are kept separate.
### Initializers
- [init?(rawValue: UInt)](./mpsrnnbidirectionalcombinemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Instance Properties
- [var bidirectionalCombineMode: MPSRNNBidirectionalCombineMode](./mpsrnnimageinferencelayer/bidirectionalcombinemode.md)
- [var numberOfLayers: Int](./mpsrnnimageinferencelayer/numberoflayers.md)
- [var recurrentOutputIsTemporary: Bool](./mpsrnnimageinferencelayer/recurrentoutputistemporary.md)
- [var storeAllIntermediateStates: Bool](./mpsrnnimageinferencelayer/storeallintermediatestates.md)
- [var inputFeatureChannels: Int](./mpsrnnimageinferencelayer/inputfeaturechannels.md)
- [var outputFeatureChannels: Int](./mpsrnnimageinferencelayer/outputfeaturechannels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnbidirectionalcombinemode)*