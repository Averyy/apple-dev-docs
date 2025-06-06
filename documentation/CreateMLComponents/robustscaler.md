# RobustScaler

**Framework**: Create ML Components  
**Kind**: struct

An estimator that scales the input using statistics that are robust to outliers.

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
struct RobustScaler<Element> where Element : BinaryFloatingPoint, Element : Decodable, Element : Encodable
```

## Topics

### Creating an estimator
- [init(quantileRange: ClosedRange<Element>)](robustscaler/init(quantilerange:).md)
  Creates a robust scaler.
### Getting the properties
- [var quantileRange: ClosedRange<Element>](robustscaler/quantilerange.md)
  The quantile range used to compute the scale.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) throws -> RobustScaler<Element>.Transformer](robustscaler/fitted(to:eventhandler:).md)
  Fits a robust scaler to a sequence of elements.
### Default Implementations
- [Estimator Implementations](robustscaler/estimator-implementations.md)

## Relationships

### Conforms To
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct StandardScaler](standardscaler.md)
  An estimator that standardizes the input by removing the mean and scaling to unit variance.
- [struct MaxAbsScaler](maxabsscaler.md)
  An estimator that scales the input values so that the maximum absolute value is 1.0.
- [struct MinMaxScaler](minmaxscaler.md)
  An estimator that scales the input values so that they all lie in a closed range.
- [struct NormalizationScaler](normalizationscaler.md)
  An estimator that normalizes the input values using a normalization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/robustscaler)*