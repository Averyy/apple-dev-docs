# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a model to a sequence of examples.

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
func fitted(to input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws -> LinearTimeSeriesForecaster<Scalar>.Model
```

#### Return Value

The fitted model.

#### Discussion

This method uses a sliding window to chunk the input features into features of [`inputWindowSize`](lineartimeseriesforecaster/inputwindowsize.md) elements and annotations of [`forecastWindowSize`](lineartimeseriesforecaster/forecastwindowsize.md) elements. If you want to use a different windowing strategy, use [`fitted(toWindows:eventHandler:)`](lineartimeseriesforecaster/fitted(towindows:eventhandler:).md).

## Parameters

- `input`: A sequence of annotated features. Each feature’s shape should be   and each   annotation’s shape should be  . This method divides the input sequence into windows.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/fitted(to:eventhandler:))*