# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this tabular estimator with a supervised tabular estimator.

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
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation> where Other : SupervisedTabularEstimator
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>> where Other : TabularEstimator
```

```swift
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>> where Other : TabularTransformer
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/appending(_:))*