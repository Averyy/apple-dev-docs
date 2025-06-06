# MLDictionaryFeatureProvider

**Framework**: Core ML  
**Kind**: class

A convenience wrapper for the given dictionary of data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class MLDictionaryFeatureProvider
```

#### Overview

If your input data is stored in a dictionary, consider this type of [`MLFeatureProvider`](mlfeatureprovider.md) that is backed by a dictionary. It is a convenience interface, saving you the trouble of iterating through the dictionary to assign all of its values.

## Topics

### Creating the Provider
- [init(dictionary: [String : Any]) throws](mldictionaryfeatureprovider/init(dictionary:).md)
  Creates the feature provider based on a dictionary.
### Accessing the Features
- [subscript(String) -> MLFeatureValue?](mldictionaryfeatureprovider/subscript(_:).md)
  Subscript interface for the feature provider to pass through to the dictionary.
- [var dictionary: [String : MLFeatureValue]](mldictionaryfeatureprovider/dictionary.md)
  The backing dictionary.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MLFeatureProvider](mlfeatureprovider.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.
- [class MLFeatureValue](mlfeaturevalue.md)
  A generic wrapper around an underlying value and the value’s type.
- [struct MLSendableFeatureValue](mlsendablefeaturevalue.md)
  A sendable feature value.
- [protocol MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.
- [protocol MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.
- [class MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mldictionaryfeatureprovider)*