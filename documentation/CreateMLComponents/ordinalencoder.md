# OrdinalEncoder

**Framework**: Create ML Components  
**Kind**: struct

An ordinal encoder estimator encodes categorical values to ordinal integer values.

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
struct OrdinalEncoder<Category> where Category : Comparable, Category : Decodable, Category : Encodable, Category : Hashable
```

## Topics

### Creating an encoder
- [init()](ordinalencoder/init.md)
  Creates an ordinal encoding estimator.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) throws -> OrdinalEncoder<Category>.Transformer](ordinalencoder/fitted(to:eventhandler:).md)
  Fits an ordinal encoder to a sequence of categories.
### Default Implementations
- [Estimator Implementations](ordinalencoder/estimator-implementations.md)
- [UpdatableEstimator Implementations](ordinalencoder/updatableestimator-implementations.md)

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
- [struct NumericImputer](numericimputer.md)
  An estimator that replaces missing values in the numeric input.
- [struct Reshaper](reshaper.md)
  A transformer that reshapes a shaped array.
- [struct CategoricalImputer](categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.
- [struct OptionalUnwrapper](optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder)*