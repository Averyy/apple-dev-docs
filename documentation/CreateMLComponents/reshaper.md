# Reshaper

**Framework**: Create ML Components  
**Kind**: struct

A transformer that reshapes a shaped array.

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
struct Reshaper<Scalar> where Scalar : MLShapedArrayScalar, Scalar : Decodable, Scalar : Encodable
```

## Topics

### Creating a transformer
- [init(shape: [Int])](reshaper/init(shape:).md)
  Creates a reshape transformer.
- [init(from: any Decoder) throws](reshaper/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Getting the shape
- [var shape: [Int]](reshaper/shape.md)
  The target shape.
### Performing the transformation
- [func applied<S>(S, eventHandler: EventHandler?) throws -> [MLShapedArray<Scalar>]](reshaper/applied(_:eventhandler:).md)
  Reshapes a sequence of inputs.
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) throws -> MLShapedArray<Scalar>](reshaper/applied(to:eventhandler:).md)
  Reshapes the input.
### Operators
- [static func == (Reshaper<Scalar>, Reshaper<Scalar>) -> Bool](reshaper/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](reshaper/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [typealias Input](reshaper/input.md)
  The input type.
- [typealias Output](reshaper/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](reshaper/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](reshaper/equatable-implementations.md)
- [Transformer Implementations](reshaper/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [Transformer](transformer.md)

## See Also

- [struct LinearTransformer](lineartransformer.md)
  A transformer that runs an input through a scale and offset.
- [struct ImputeTransformer](imputetransformer.md)
  A transformer that replaces missing values with a pre-defined value.
- [struct OneHotEncoder](onehotencoder.md)
  An estimator that encodes categorical values to an integer array.
- [struct OrdinalEncoder](ordinalencoder.md)
  An ordinal encoder estimator encodes categorical values to ordinal integer values.
- [struct NumericImputer](numericimputer.md)
  An estimator that replaces missing values in the numeric input.
- [struct CategoricalImputer](categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.
- [struct OptionalUnwrapper](optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/reshaper)*