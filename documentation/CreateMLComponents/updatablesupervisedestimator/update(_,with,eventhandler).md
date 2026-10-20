# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates a transformer with a new sequence of examples.

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
func update<InputSequence>(_ transformer: inout Self.Transformer, with input: InputSequence, eventHandler: EventHandler?) async throws where InputSequence : Sequence, InputSequence.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>
```

## Mentions

- [Augmenting images to expand your training data](../augmenting-images-to-expand-your-training-data.md)

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## Default Implementations

### UpdatableSupervisedEstimator Implementations
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29-483v7.md)
  Updates a transformer on an async sequence of examples.

## See Also

### Transforming
- [func makeTransformer() -> Self.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](./update%28_,with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimator/update(_:with:eventhandler:))*