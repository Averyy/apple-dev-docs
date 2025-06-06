# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a numeric imputer to a sequence of elements.

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
func fitted<S>(to input: S, eventHandler: EventHandler? = nil) -> NumericImputer<Element>.Transformer where S : Sequence, S.Element == Element?
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of elements.
- `eventHandler`: An event handler.

## See Also

- [NumericImputer.Transformer](numericimputer/transformer.md)
  The transformer type created by this estimator.
- [NumericImputer.Strategy](numericimputer/strategy-swift.enum.md)
  An imputation strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/fitted(to:eventhandler:))*