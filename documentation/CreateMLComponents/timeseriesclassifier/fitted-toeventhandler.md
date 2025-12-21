# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a time series classifier model to a sequence of examples.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func fitted(to input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler? = nil) async throws -> TimeSeriesClassifier<Scalar, Label>.Model
```

#### Return Value

The fitted time series classifier model.

#### Discussion

The training process partitions the input into random batches according to the batch size configuration parameter. Training stops when the validation loss stops improving or when the maximum number of iterations is reached.

## Parameters

- `input`: A sequence of annotated features for training. Each feature’s shape should be    and each annotation should be one-hot encoded with shape  .
- `eventHandler`: An event handler.

## See Also

- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler?) async throws -> TimeSeriesClassifier<Scalar, Label>.Model](timeseriesclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a time series classifier model to a sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/fitted(to:eventhandler:))*