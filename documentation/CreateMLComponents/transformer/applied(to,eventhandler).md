# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Performs the transformation on a single input.

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
func applied(to input: Self.Input, eventHandler: EventHandler?) async throws -> Self.Output
```

## Return Value

An output produced by applying the transformer to the input.

## Parameters

- `input`: The transformer input.
- `eventHandler`: An event handler.

## Default Implementations

### Transformer Implementations
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.Output]](./applied%28to,eventhandler%29-274uv.md)
  Performs the transformation on a sequence of inputs.
- [func applied<S, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.Output, Annotation>]](./applied%28to,eventhandler%29-gcy8.md)
  Performs the transformation on a sequence of annotated inputs.

## See Also

### Applying and adapting
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](./adaptedasannotatedfeaturetransformer%28annotationtype%29.md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](./adaptedasannotatedpredictiontransformer%28annotationtype%29.md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](./adaptedasestimator%28%29.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](./adaptedasrandomtransformer%28%29.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal()](./adaptedastemporal%28%29.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](./adaptedasupdatableestimator%28%29.md)
  Exposes this transformer as a trivial estimator.
- [associatedtype Input](./input.md)
  The input type.
- [associatedtype Output](./output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/applied(to:eventhandler:))*