# appending(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Composes this transformer with an estimator.

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
func appending<Other>(_ other: Other) -> PreprocessingTabularEstimator<Self, Other> where Other : TabularEstimator
```

**Other overloads**:

```swift
func appending<Other>(_ other: Other) -> ComposedTabularTransformer<Self, Other> where Other : TabularTransformer
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingSupervisedTabularEstimator<Self, Other> where Other : SupervisedTabularEstimator
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other> where Other : UpdatableSupervisedTabularEstimator
```

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableTabularEstimator<Self, Other> where Other : UpdatableTabularEstimator
```

```swift
func appending<Other>(_ other: Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation> where Other : SupervisedTabularEstimator
```

```swift
func appending<Other>(_ other: Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>> where Other : TabularEstimator
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformer/appending(_:)-5xcrt)*