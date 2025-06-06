# CategoricalImputer

**Framework**: Create ML Components  
**Kind**: struct

An estimator that replaces missing values in the categorical input.

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
struct CategoricalImputer<Element> where Element : Decodable, Element : Encodable, Element : Hashable
```

## Topics

### Creating an estimator
- [init(CategoricalImputer<Element>.Strategy)](categoricalimputer/init(_:).md)
  Creates an imputer with a strategy.
- [init(constant: Element)](categoricalimputer/init(constant:).md)
  Creates an imputer with a constant value to use when replacing missing values.
### Getting the properties
- [var strategy: CategoricalImputer<Element>.Strategy](categoricalimputer/strategy-swift.property.md)
  The imputation strategy.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) -> CategoricalImputer<Element>.Transformer](categoricalimputer/fitted(to:eventhandler:).md)
  Fits a categorical imputer to a sequence of elements.
- [CategoricalImputer.Transformer](categoricalimputer/transformer.md)
  The transformer type created by this estimator.
- [CategoricalImputer.Strategy](categoricalimputer/strategy-swift.enum.md)
  An imputation strategy.
### Default Implementations
- [CustomDebugStringConvertible Implementations](categoricalimputer/customdebugstringconvertible-implementations.md)
- [Estimator Implementations](categoricalimputer/estimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct Reshaper](reshaper.md)
  A transformer that reshapes a shaped array.
- [struct OptionalUnwrapper](optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/categoricalimputer)*