# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a model with a sequence of features.

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
func update(_ model: inout LinearTimeSeriesForecaster<Scalar>.Model, with input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws
```

#### Discussion

This method uses a sliding window to chunk the input features into features of [`inputWindowSize`](lineartimeseriesforecaster/inputwindowsize.md) elements and annotations of [`forecastWindowSize`](lineartimeseriesforecaster/forecastwindowsize.md) elements. If you want to use a different windowing strategy, use [`update(_:withWindows:eventHandler:)`](lineartimeseriesforecaster/update(_:withwindows:eventhandler:).md).

## Parameters

- `model`: The model to update.
- `input`: A sequence of annotated features. The feature shape must be   and the annotation shape   must be  .
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/update(_:with:eventhandler:))*