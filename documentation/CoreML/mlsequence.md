# MLSequence

**Framework**: Core ML  
**Kind**: class

A machine learning collection type that stores a series of strings or integers.

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
class MLSequence
```

#### Overview

A sequence stores a series of integers or strings of any length as the underlying type of an `MLFeatureValue`. Some classifier models — typically natural language models, such as an [`NLTagger`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger) — produce an [`MLSequence`](mlsequence.md) feature value from their output features.

## Topics

### Creating a sequence
- [convenience init(strings: [String])](mlsequence/init(strings:).md)
  Creates a sequence of strings from a string array.
- [convenience init(int64s: [NSNumber])](mlsequence/init(int64s:).md)
  Creates a sequence of integers from an array of numbers.
- [convenience init(empty: MLFeatureType)](mlsequence/init(empty:).md)
  Creates an empty sequence of strings or integers.
### Identifying the sequence’s element type
- [var type: MLFeatureType](mlsequence/type.md)
  The underlying type of the sequence’s elements.
### Retrieving the Sequence’s Values
- [var stringValues: [String]](mlsequence/stringvalues.md)
  An array of strings in the sequence.
- [var int64Values: [NSNumber]](mlsequence/int64values.md)
  An array of 64-bit integers in the sequence.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [enum MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [struct MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.
- [protocol MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.
- [class MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequence)*