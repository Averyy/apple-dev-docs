# LinearTransformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that runs an input through a scale and offset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct LinearTransformer<Element> where Element : BinaryFloatingPoint, Element : Decodable, Element : Encodable
```

## Topics

### Creating a regressor
- [init(scale: Element, offset: Element)](lineartransformer/init(scale:offset:).md)
  Creates a linear transformer.
### Getting the properties
- [var offset: Element](lineartransformer/offset.md)
  The amount to be offset after scaling.
- [var scale: Element](lineartransformer/scale.md)
  The amount to be scaled.
### Performing the transformation
- [func applied(to:eventHandler:)](lineartransformer/applied(to:eventhandler:).md)
  Scales an input.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)

## See Also

- [struct ImputeTransformer](imputetransformer.md)
  A transformer that replaces missing values with a pre-defined value.
- [struct OneHotEncoder](onehotencoder.md)
  An estimator that encodes categorical values to an integer array.
- [struct OrdinalEncoder](ordinalencoder.md)
  An ordinal encoder estimator encodes categorical values to ordinal integer values.
- [struct NumericImputer](numericimputer.md)
  An estimator that replaces missing values in the numeric input.
- [struct Reshaper](reshaper.md)
  A transformer that reshapes a shaped array.
- [struct CategoricalImputer](categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.
- [struct OptionalUnwrapper](optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartransformer)*