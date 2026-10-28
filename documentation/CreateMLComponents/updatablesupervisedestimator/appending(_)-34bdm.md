# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this updatable supervised estimator with a temporal transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
@preconcurrency
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation> where Other : TemporalTransformer, Self.Annotation : Sendable, Other.Input == Self.Transformer.Output
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation> where Other : UpdatableEstimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation> where Other : UpdatableSupervisedEstimator, Self.Annotation == Other.Annotation, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation> where Other : Transformer, Other.Input == Self.Transformer.Output
```

```swift
@preconcurrency
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation> where Other : UpdatableTemporalEstimator, Self.Annotation : Sendable, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation> where Other : UpdatableSupervisedTemporalEstimator, Self.Annotation == Other.Annotation, Self.Transformer.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimator/appending(_:)-34bdm)*