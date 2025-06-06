# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a categorical imputer to a sequence of elements.

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
func fitted<S>(to input: S, eventHandler: EventHandler? = nil) -> CategoricalImputer<Element>.Transformer where S : Sequence, S.Element == Element?
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of elements.
- `eventHandler`: An event handler.

## See Also

- [CategoricalImputer.Transformer](categoricalimputer/transformer.md)
  The transformer type created by this estimator.
- [CategoricalImputer.Strategy](categoricalimputer/strategy-swift.enum.md)
  An imputation strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/categoricalimputer/fitted(to:eventhandler:))*