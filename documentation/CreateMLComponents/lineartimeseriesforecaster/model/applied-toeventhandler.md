# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

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

#### Return Value

A shaped array of predictions with shape `[M, forecastWindowSize, annotationSize]` where `M` is the number of predictions based on the input sequence length and the [`stride`](lineartimeseriesforecaster/model/stride.md) property.

#### Discussion

This method uses a sliding window to chunk the input features into [`inputWindowSize`](lineartimeseriesforecaster/model/inputwindowsize.md) elements every [`stride`](lineartimeseriesforecaster/model/stride.md) elements. If you want to use a different windowing strategy, use [`applied(toWindow:eventHandler:)`](lineartimeseriesforecaster/model/applied(towindow:eventhandler:).md).

## Parameters

- `input`: An shaped array of features. The shape must be   where   is the length of the   sequence, which must be at least  .
- `eventHandler`: An event handler.

## See Also

- [func applied(toWindow: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](lineartimeseriesforecaster/model/applied(towindow:eventhandler:).md)
  Performs a prediction on a window of input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/applied(to:eventhandler:))*