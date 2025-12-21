# MLSendableFeatureValue

**Framework**: Core ML  
**Kind**: struct

A sendable feature value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MLSendableFeatureValue
```

#### Overview

This version of feature value is similar to [`MLFeatureValue`](mlfeaturevalue.md) but it can be passed across concurrency domains. Once in the target concurrency domain, you can then convert it to a [`MLFeatureValue`](mlfeaturevalue.md).

## Topics

### Creating a sendable feature value
- [init(_:)](mlsendablefeaturevalue/init(_:).md)
  Creates a feature value containing a double-precision floating-point value.
- [init(undefined: MLFeatureType)](mlsendablefeaturevalue/init(undefined:).md)
  Creates an undefined feature value of a specific type.
### Accessing the values
- [var doubleValue: Double?](mlsendablefeaturevalue/doublevalue.md)
  The double-precision floating-point value, if the contained value is a double.
- [var float16Value: Float16?](mlsendablefeaturevalue/float16value.md)
  The 16-bit floating-point value, if the contained value is a 16-bit float.
- [var floatValue: Float?](mlsendablefeaturevalue/floatvalue.md)
  The single-precision floating-point value, if the contained value is a float.
- [var integerDictionaryValue: [Int : Double]?](mlsendablefeaturevalue/integerdictionaryvalue.md)
  The integer dictionary value, if the contained value is a dictionary of integers to numbers.
- [var integerValue: Int?](mlsendablefeaturevalue/integervalue.md)
  The integer value, if the contained value is an integer.
- [var isScalar: Bool](mlsendablefeaturevalue/isscalar.md)
  A Boolean value indicating whether the value is a single number.
- [var isShapedArray: Bool](mlsendablefeaturevalue/isshapedarray.md)
  A Boolean value indicating whether the value is a shaped array.
- [var isUndefined: Bool](mlsendablefeaturevalue/isundefined.md)
  A Boolean value indicating whether the value is missing or undefined.
- [var stringArrayValue: [String]?](mlsendablefeaturevalue/stringarrayvalue.md)
  The string array value, if the contained value is an array of string.
- [var stringDictionaryValue: [String : Double]?](mlsendablefeaturevalue/stringdictionaryvalue.md)
  The string dictionary value, if the contained value is a dictionary of strings to numbers.
- [var stringValue: String?](mlsendablefeaturevalue/stringvalue.md)
  The string value, if the contained value is a string.
- [var type: MLFeatureType](mlsendablefeaturevalue/type.md)
  The type of value.
### Getting the shaped array value
- [func shapedArrayValue<Scalar>(of: Scalar.Type) -> MLShapedArray<Scalar>?](mlsendablefeaturevalue/shapedarrayvalue(of:).md)
  Returns the shaped array value, if the contained value is a shaped array of the specified type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.
- [class MLFeatureValue](mlfeaturevalue.md)
  A generic wrapper around an underlying value and the value’s type.
- [protocol MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.
- [class MLDictionaryFeatureProvider](mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.
- [protocol MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.
- [class MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsendablefeaturevalue)*