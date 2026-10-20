# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Performs a prediction on a shaped array of features.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> MLShapedArray<Scalar>
```

**Other overloads**:

```swift
func applied(to input: some Sequence<MLShapedArray<Scalar>>, eventHandler: EventHandler? = nil) async throws -> [MLShapedArray<Scalar>]
```

```swift
func applied(to input: some TemporalSequence<MLShapedArray<Scalar>>, eventHandler: EventHandler? = nil) async throws -> AnyTemporalSequence<MLShapedArray<Scalar>>
```

#### Return Value

A shaped array of predictions with shape `[M, forecastWindowSize, annotationSize]` where `M` is the number of predictions based on the input sequence length and the [`stride`](./stride.md) property.

#### Discussion

This method uses a sliding window to chunk the input features into [`inputWindowSize`](./inputwindowsize.md) elements every [`stride`](./stride.md) elements. If you want to use a different windowing strategy, use [`applied(toWindow:eventHandler:)`](./applied%28towindow,eventhandler%29.md).

## Parameters

- `input`: An shaped array of features. The shape must be `[N, featureSize]` where `N` is the length of the sequence, which must be at least `inputWindowSize`.
- `eventHandler`: An event handler.

## See Also

### Applying the model
- [func applied(toWindow: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](./applied%28towindow,eventhandler%29.md)
  Performs a prediction on a window of input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/applied(to:eventhandler:))*