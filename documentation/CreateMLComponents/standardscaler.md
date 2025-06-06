# StandardScaler

**Framework**: Create ML Components  
**Kind**: struct

An estimator that standardizes the input by removing the mean and scaling to unit variance.

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
struct StandardScaler<Element> where Element : BinaryFloatingPoint, Element : Decodable, Element : Encodable
```

## Topics

### Creating an estimator
- [init()](standardscaler/init.md)
  Creates a standard scaling estimator.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) throws -> StandardScaler<Element>.Transformer](standardscaler/fitted(to:eventhandler:).md)
  Fits a transformer to a particular input sequence by computing the mean and standard deviation.
### Default Implementations
- [Estimator Implementations](standardscaler/estimator-implementations.md)
- [UpdatableEstimator Implementations](standardscaler/updatableestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)
- [UpdatableEstimator](updatableestimator.md)

## See Also

- [struct MaxAbsScaler](maxabsscaler.md)
  An estimator that scales the input values so that the maximum absolute value is 1.0.
- [struct MinMaxScaler](minmaxscaler.md)
  An estimator that scales the input values so that they all lie in a closed range.
- [struct NormalizationScaler](normalizationscaler.md)
  An estimator that normalizes the input values using a normalization strategy.
- [struct RobustScaler](robustscaler.md)
  An estimator that scales the input using statistics that are robust to outliers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler)*