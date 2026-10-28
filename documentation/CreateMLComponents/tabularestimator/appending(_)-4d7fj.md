# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Compose this tabular estimator with a tabular transformer.

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
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>> where Other : TabularTransformer
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation> where Other : SupervisedTabularEstimator
```

```swift
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>> where Other : TabularEstimator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/appending(_:)-4d7fj)*