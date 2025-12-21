# MLBatchProvider

**Framework**: Core ML  
**Kind**: protocol

An interface that represents a collection of feature providers.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
protocol MLBatchProvider
```

#### Overview

Similar to the [`MLFeatureProvider`](mlfeatureprovider.md), this interface allows you to define your own batch provider. If you collect your data asynchronously or it is memory intensive, implement this protocol on your data structure to optimize performance with batch processing.

## Topics

### Accessing values
- [func features(at: Int) -> any MLFeatureProvider](mlbatchprovider/features(at:).md)
  Returns the feature provider at the given index.
- [var count: Int](mlbatchprovider/count.md)
  The number of feature providers in this batch.

## Relationships

### Conforming Types
- [MLArrayBatchProvider](mlarraybatchprovider.md)

## See Also

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.
- [class MLFeatureValue](mlfeaturevalue.md)
  A generic wrapper around an underlying value and the value’s type.
- [struct MLSendableFeatureValue](mlsendablefeaturevalue.md)
  A sendable feature value.
- [protocol MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.
- [class MLDictionaryFeatureProvider](mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.
- [class MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.
- [class MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlbatchprovider)*