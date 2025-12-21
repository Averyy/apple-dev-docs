# MLArrayBatchProvider

**Framework**: Core ML  
**Kind**: class

A convenience wrapper for batches of feature providers.

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
class MLArrayBatchProvider
```

#### Overview

This batch provider supports an array of feature providers or a dictionary of arrays of feature values.

## Topics

### Creating a batch provider
- [init(array: [any MLFeatureProvider])](mlarraybatchprovider/init(array:).md)
  Creates the batch provider based on the array of feature providers.
- [init(dictionary: [String : [Any]]) throws](mlarraybatchprovider/init(dictionary:).md)
  Creates a batch provider based on feature names and their associated arrays of data.
### Accessing the feature providers
- [var array: [any MLFeatureProvider]](mlarraybatchprovider/array.md)
  The array of feature providers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MLBatchProvider](mlbatchprovider.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [protocol MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlarraybatchprovider)*