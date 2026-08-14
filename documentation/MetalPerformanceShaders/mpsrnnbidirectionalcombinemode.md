# MPSRNNBidirectionalCombineMode

**Framework**: Metal Performance Shaders  
**Kind**: enum

Modes that define how two images or matrices are combined.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSRNNBidirectionalCombineMode
```

## Topics

### Enumeration Cases
- [MPSRNNBidirectionalCombineMode.add](mpsrnnbidirectionalcombinemode/add.md)
  A mode in which two sequences are summed to form a single output.
- [MPSRNNBidirectionalCombineMode.concatenate](mpsrnnbidirectionalcombinemode/concatenate.md)
  A mode in which two sequences are concatenated along the feature channels to form a single output.
- [MPSRNNBidirectionalCombineMode.none](mpsrnnbidirectionalcombinemode/none.md)
  A mode in which two sequences are kept separate.
### Initializers
- [init?(rawValue: UInt)](mpsrnnbidirectionalcombinemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var bidirectionalCombineMode: MPSRNNBidirectionalCombineMode](mpsrnnimageinferencelayer/bidirectionalcombinemode.md)
- [var numberOfLayers: Int](mpsrnnimageinferencelayer/numberoflayers.md)
- [var recurrentOutputIsTemporary: Bool](mpsrnnimageinferencelayer/recurrentoutputistemporary.md)
- [var storeAllIntermediateStates: Bool](mpsrnnimageinferencelayer/storeallintermediatestates.md)
- [var inputFeatureChannels: Int](mpsrnnimageinferencelayer/inputfeaturechannels.md)
- [var outputFeatureChannels: Int](mpsrnnimageinferencelayer/outputfeaturechannels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnbidirectionalcombinemode)*