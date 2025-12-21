# NumericImputer

**Framework**: Create ML Components  
**Kind**: struct

An estimator that replaces missing values in the numeric input.

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
struct NumericImputer<Element> where Element : BinaryFloatingPoint, Element : Decodable, Element : Encodable
```

## Topics

### Creating an estimator
- [init(NumericImputer<Element>.Strategy)](numericimputer/init(_:).md)
  Creates an imputer with a strategy.
- [init(constant: Element)](numericimputer/init(constant:).md)
  Creates an imputer with a constant value to use when replacing missing values.
### Getting the properties
- [var strategy: NumericImputer<Element>.Strategy](numericimputer/strategy-swift.property.md)
  The imputation strategy.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) -> NumericImputer<Element>.Transformer](numericimputer/fitted(to:eventhandler:).md)
  Fits a numeric imputer to a sequence of elements.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.
- [NumericImputer.Strategy](numericimputer/strategy-swift.enum.md)
  An imputation strategy.
### Default Implementations
- [UpdatableEstimator Implementations](numericimputer/updatableestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UpdatableEstimator](updatableestimator.md)

## See Also

- [struct LinearTransformer](lineartransformer.md)
  A transformer that runs an input through a scale and offset.
- [struct ImputeTransformer](imputetransformer.md)
  A transformer that replaces missing values with a pre-defined value.
- [struct OneHotEncoder](onehotencoder.md)
  An estimator that encodes categorical values to an integer array.
- [struct OrdinalEncoder](ordinalencoder.md)
  An ordinal encoder estimator encodes categorical values to ordinal integer values.
- [struct Reshaper](reshaper.md)
  A transformer that reshapes a shaped array.
- [struct CategoricalImputer](categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.
- [struct OptionalUnwrapper](optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer)*