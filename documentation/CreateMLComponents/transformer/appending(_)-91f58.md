# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this transformer with an annotated-feature transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other, Annotation>(_ other: Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output> where Other : Transformer, Other.Input == AnnotatedPrediction<Self.Output, Annotation>
```

**Other overloads**:

```swift
func appending<Other, Annotation>(_ other: Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output> where Other : Transformer, Other.Input == AnnotatedFeature<Self.Output, Annotation>
```

```swift
func appending<Other, Annotation>(_ other: Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>> where Other : Transformer, Self.Output == AnnotatedFeature<Other.Input, Annotation>
```

```swift
func appending<Other, Annotation>(_ other: Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>> where Other : Transformer, Self.Output == AnnotatedPrediction<Other.Input, Annotation>
```

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other> where Self : Sendable, Other : TemporalTransformer, Self.Output == Other.Input
```

```swift
func appending<Other>(_ other: Other) -> ComposedTransformer<Self, Other> where Other : Transformer, Self.Output == Other.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingEstimator<Self, Other> where Other : Estimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingSupervisedEstimator<Self, Other> where Other : SupervisedEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableEstimator<Self, Other> where Other : UpdatableEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other> where Other : UpdatableSupervisedEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other> where Other : TemporalTransformer, Self.Output == Other.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other> where Other : SupervisedTemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other> where Other : TemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other> where Other : UpdatableSupervisedTemporalEstimator, Self.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other> where Other : UpdatableTemporalEstimator, Self.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/appending(_:)-91f58)*