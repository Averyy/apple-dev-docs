# NormalizationScaler

**Framework**: Create ML Components  
**Kind**: struct

An estimator that normalizes the input values using a normalization strategy.

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
struct NormalizationScaler<Element> where Element : BinaryFloatingPoint, Element : Decodable, Element : Encodable
```

## Topics

### Creating a scaler
- [init(norm: NormalizationScaler<Element>.NormalizationStrategy)](normalizationscaler/init(norm:).md)
  Creates a normalization scaler.
- [NormalizationScaler.NormalizationStrategy](normalizationscaler/normalizationstrategy.md)
  A normalization strategy.
### Getting the normalization
- [var norm: NormalizationScaler<Element>.NormalizationStrategy](normalizationscaler/norm.md)
  The normalization strategy.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) throws -> NormalizationScaler<Element>.Transformer](normalizationscaler/fitted(to:eventhandler:).md)
  Fits a normalization scaler to a sequence of elements.
### Default Implementations
- [Estimator Implementations](normalizationscaler/estimator-implementations.md)

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
- [struct RobustScaler](robustscaler.md)
  An estimator that scales the input using statistics that are robust to outliers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler)*