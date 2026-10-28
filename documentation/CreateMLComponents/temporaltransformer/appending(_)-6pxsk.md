# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this temporal transformer with an estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func appending<Other>(_ other: Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>> where Other : Estimator, Self.Output == Other.Transformer.Input
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<Self, Other> where Other : TemporalTransformer, Self.Output == Other.Input
```

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<Self, TemporalAdaptor<Other>> where Other : Transformer, Other : Sendable, Self.Output == Other.Input
```

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>> where Other : Transformer, Self.Output == Other.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other> where Other : SupervisedTemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>> where Other : SupervisedEstimator, Self.Output == Other.Transformer.Input, Other.Annotation : Sendable
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingTemporalEstimator<Self, Other> where Other : TemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other> where Other : UpdatableSupervisedTemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>> where Other : UpdatableSupervisedEstimator, Self.Output == Other.Transformer.Input, Other.Annotation : Sendable
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other> where Other : UpdatableTemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>> where Other : UpdatableEstimator, Self.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/appending(_:)-6pxsk)*