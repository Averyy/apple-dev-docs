# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this supervised estimator with a transformer.

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
func appending<Other>(_ other: Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation> where Other : Transformer, Other.Input == Self.Transformer.Output
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation> where Other : Estimator, Self.Transformer.Output == Other.Transformer.Input
```

```swift
func appending<Other>(_ other: Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation> where Other : SupervisedEstimator, Self.Annotation == Other.Annotation, Self.Transformer.Output == Other.Transformer.Input
```

```swift
@preconcurrency
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation> where Other : TemporalEstimator, Self.Annotation : Sendable, Self.Transformer.Output == Other.Transformer.Input
```

```swift
@preconcurrency
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation> where Other : TemporalTransformer, Self.Annotation : Sendable, Other.Input == Self.Transformer.Output
```

```swift
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation> where Other : SupervisedTemporalEstimator, Self.Annotation == Other.Annotation, Self.Transformer.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator/appending(_:)-629ia)*