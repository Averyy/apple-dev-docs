# OneHotEncoder

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An estimator that encodes categorical values to an integer array.

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
struct OneHotEncoder<Category> where Category : Comparable, Category : Decodable, Category : Encodable, Category : Hashable
```

## Overview

The encoded array has an element count equal to the number of categories to encode. The encoded array for a given category has repeating zero values except at one index where the value is 1.

## Topics

### Creating the estimator
- [init()](./onehotencoder/init%28%29.md)
  Creates a one-hot encoding estimator.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) throws -> OneHotEncoder<Category>.Transformer](./onehotencoder/fitted%28to,eventhandler%29.md)
  Fits a one-hot encoder to a sequence of categories.
### Default Implementations
- [Estimator Implementations](./onehotencoder/estimator-implementations.md)
- [UpdatableEstimator Implementations](./onehotencoder/updatableestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Estimator](./estimator.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UpdatableEstimator](./updatableestimator.md)

## See Also

### Preprocessors
- [struct LinearTransformer](./lineartransformer.md)
  A transformer that runs an input through a scale and offset.
- [struct ImputeTransformer](./imputetransformer.md)
  A transformer that replaces missing values with a pre-defined value.
- [struct OrdinalEncoder](./ordinalencoder.md)
  An ordinal encoder estimator encodes categorical values to ordinal integer values.
- [struct NumericImputer](./numericimputer.md)
  An estimator that replaces missing values in the numeric input.
- [struct Reshaper](./reshaper.md)
  A transformer that reshapes a shaped array.
- [struct CategoricalImputer](./categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.
- [struct OptionalUnwrapper](./optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder)*