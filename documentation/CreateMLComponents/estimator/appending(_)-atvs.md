# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this estimator with a supervised estimator.

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
func appending<Other>(_ other: Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation> where Other : SupervisedEstimator, Self.Transformer.Output == Other.Transformer.Input
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>> where Other : Estimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>> where Other : Transformer, Other.Input == Self.Transformer.Output
```

```swift
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation> where Other : SupervisedTemporalEstimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>> where Other : TemporalEstimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>> where Other : TemporalTransformer, Other.Input == Self.Transformer.Output
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/appending(_:)-atvs)*