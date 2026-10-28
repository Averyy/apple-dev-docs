# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this updatable estimator with an updatable temporal estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func appending<Other>(_ other: Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>> where Other : UpdatableTemporalEstimator, Self.Transformer.Output == Other.Transformer.Input
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>> where Other : UpdatableEstimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>> where Other : Transformer, Other.Input == Self.Transformer.Output
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation> where Other : UpdatableSupervisedEstimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation> where Other : UpdatableSupervisedTemporalEstimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>> where Other : TemporalTransformer, Other.Input == Self.Transformer.Output
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimator/appending(_:)-2zfb9)*