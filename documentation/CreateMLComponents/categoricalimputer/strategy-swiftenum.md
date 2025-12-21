# CategoricalImputer.Strategy

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
- [CategoricalImputer.Strategy.constant(_:)](categoricalimputer/strategy-swift.enum/constant(_:).md)
  Imputation strategy that replaces missing elements with a constant.
- [CategoricalImputer.Strategy.mode](categoricalimputer/strategy-swift.enum/mode.md)
  Imputation strategy that replaces missing elements with the mode.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fitted<S>(to: S, eventHandler: EventHandler?) -> CategoricalImputer<Element>.Transformer](categoricalimputer/fitted(to:eventhandler:).md)
  Fits a categorical imputer to a sequence of elements.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/categoricalimputer/strategy-swift.enum)*