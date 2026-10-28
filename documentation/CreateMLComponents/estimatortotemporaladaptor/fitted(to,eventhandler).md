# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Fits a transformer to a sequence of examples.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func fitted<InputSequence>(to input: InputSequence, eventHandler: EventHandler? = nil) async throws -> EstimatorToTemporalAdaptor<Base>.Transformer where InputSequence : Sequence, InputSequence.Element : TemporalSequence, Base.Transformer.Input == InputSequence.Element.Feature
```

## Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

### Fitting a transformer
- [EstimatorToTemporalAdaptor.Input](./input.md)
  The input type.
- [EstimatorToTemporalAdaptor.Output](./output.md)
  The output type.
- [EstimatorToTemporalAdaptor.Transformer](./transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortotemporaladaptor/fitted(to:eventhandler:))*