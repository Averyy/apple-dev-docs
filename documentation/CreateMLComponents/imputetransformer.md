# ImputeTransformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that replaces missing values with a pre-defined value.

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
struct ImputeTransformer<Element> where Element : Decodable, Element : Encodable
```

## Topics

### Creating a transformer
- [init(from: any Decoder) throws](imputetransformer/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(value: Element)](imputetransformer/init(value:).md)
  Creates an impute transformer.
### Getting the impute value
- [var value: Element](imputetransformer/value.md)
  Impute value used to replace missing values.
### Performing the transformation
- [func applied(to: Element?, eventHandler: EventHandler?) -> Element](imputetransformer/applied(to:eventhandler:).md)
  Imputes a single input.
### Instance Methods
- [func encode(to: any Encoder) throws](imputetransformer/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [ImputeTransformer.Input](imputetransformer/input.md)
  The input type.
- [ImputeTransformer.Output](imputetransformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](imputetransformer/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](imputetransformer/equatable-implementations.md)
- [Hashable Implementations](imputetransformer/hashable-implementations.md)
- [Transformer Implementations](imputetransformer/transformer-implementations.md)

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

- [struct LinearTransformer](lineartransformer.md)
  A transformer that runs an input through a scale and offset.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imputetransformer)*