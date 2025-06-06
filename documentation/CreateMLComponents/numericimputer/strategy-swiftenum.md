# NumericImputer.Strategy

**Framework**: Create ML Components  
**Kind**: enum

An imputation strategy.

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
enum Strategy
```

## Topics

### Imputer strategies
- [NumericImputer.Strategy.constant(_:)](numericimputer/strategy-swift.enum/constant(_:).md)
  Imputation strategy that replaces missing elements with a constant.
- [NumericImputer.Strategy.mean](numericimputer/strategy-swift.enum/mean.md)
  Imputation strategy that replaces missing elements with the mean.
- [NumericImputer.Strategy.median](numericimputer/strategy-swift.enum/median.md)
  Imputation strategy that replaces missing elements with the median.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func fitted<S>(to: S, eventHandler: EventHandler?) -> NumericImputer<Element>.Transformer](numericimputer/fitted(to:eventhandler:).md)
  Fits a numeric imputer to a sequence of elements.
- [NumericImputer.Transformer](numericimputer/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/strategy-swift.enum)*