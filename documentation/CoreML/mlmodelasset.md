# MLModelAsset

**Framework**: Core ML  
**Kind**: class

An abstraction of a compiled Core ML model asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class MLModelAsset
```

#### Overview

[`MLModelAsset`](mlmodelasset.md) provides a unified interface by abstracting the compiled model representations for `.mlmodelc` files and in-memory representations.

To use an in-memory model, create an [`MLModelAsset`](mlmodelasset.md) with an in-memory model specification, then call [`load(_:configuration:completionHandler:)`](mlmodel/load(_:configuration:completionhandler:).md).

## Topics

### Creating a model asset
- [convenience init(specification: Data) throws](mlmodelasset/init(specification:).md)
  Creates a model asset from an in-memory model specification.
- [convenience init(specification: Data, blobMapping: [URL : Data]) throws](mlmodelasset/init(specification:blobmapping:).md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.
- [convenience init(url: URL) throws](mlmodelasset/init(url:).md)
  Constructs a ModelAsset from a compiled model URL.
### Getting function names
- [func functionNames(completionHandler: ([String]?, (any Error)?) -> Void)](mlmodelasset/functionnames(completionhandler:).md)
  The list of function names in the model asset.
### Getting the model description
- [func modelDescription(completionHandler: (MLModelDescription?, (any Error)?) -> Void)](mlmodelasset/modeldescription(completionhandler:).md)
  The default model descripton.
- [func modelDescription(ofFunctionNamed: String, completionHandler: (MLModelDescription?, (any Error)?) -> Void)](mlmodelasset/modeldescription(offunctionnamed:completionhandler:).md)
  The model descripton for a specified function.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [class MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset)*