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
- [init(from: any Decoder) throws](lineartransformer/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(scale: Element, offset: Element)](lineartransformer/init(scale:offset:).md)
  Creates a linear transformer.
### Getting the properties
- [var offset: Element](lineartransformer/offset.md)
  The amount to be offset after scaling.
- [var scale: Element](lineartransformer/scale.md)
  The amount to be scaled.
### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) -> [Element]](lineartransformer/applied(to:eventhandler:)-3p0ia.md)
  Scales a sequence of inputs.
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](lineartransformer/applied(to:eventhandler:)-6w4yg.md)
  Scales an input.
### Operators
- [static func == (LinearTransformer<Element>, LinearTransformer<Element>) -> Bool](lineartransformer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](lineartransformer/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](lineartransformer/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](lineartransformer/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [LinearTransformer.Input](lineartransformer/input.md)
  The input type.
- [LinearTransformer.Output](lineartransformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](lineartransformer/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](lineartransformer/equatable-implementations.md)
- [Transformer Implementations](lineartransformer/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
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