# MinMaxScaler

**Framework**: Create ML Components  
**Kind**: struct

An estimator that scales the input values so that they all lie in a closed range.

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
struct MinMaxScaler<Element> where Element : BinaryFloatingPoint, Element : Decodable, Element : Encodable
```

## Topics

### Creating an estimator
- [init(range: ClosedRange<Element>)](minmaxscaler/init(range:).md)
  Creates a min max scaler.
### Getting the properties
- [var range: ClosedRange<Element>](minmaxscaler/range.md)
  The desired range of transformed values.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) throws -> MinMaxScaler<Element>.Transformer](minmaxscaler/fitted(to:eventhandler:).md)
  Fits a min max scaler to a sequence of elements.
### Default Implementations
- [Estimator Implementations](minmaxscaler/estimator-implementations.md)

## Relationships

### Conforms To
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct StandardScaler](standardscaler.md)
  An estimator that standardizes the input by removing the mean and scaling to unit variance.
- [struct MaxAbsScaler](maxabsscaler.md)
  An estimator that scales the input values so that the maximum absolute value is 1.0.
- [struct NormalizationScaler](normalizationscaler.md)
  An estimator that normalizes the input values using a normalization strategy.
- [struct RobustScaler](robustscaler.md)
  An estimator that scales the input using statistics that are robust to outliers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler)*