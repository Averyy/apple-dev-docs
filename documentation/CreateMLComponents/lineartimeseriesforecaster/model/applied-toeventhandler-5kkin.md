# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction on a sequence of input features.

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
func applied(to input: some Sequence<MLShapedArray<Scalar>>, eventHandler: EventHandler? = nil) async throws -> [MLShapedArray<Scalar>]
```

#### Return Value

An array of predictions. Each prediction’s shape is `[forecastWindowSize, annotationSize]`. The number of predictions depends on the input sequence length and the [`stride`](lineartimeseriesforecaster/model/stride.md) property.

#### Discussion

This method uses a sliding window to chunk the input features into [`inputWindowSize`](lineartimeseriesforecaster/model/inputwindowsize.md) elements every [`stride`](lineartimeseriesforecaster/model/stride.md) elements. If you want to use a different windowing strategy, use [`applied(toWindow:eventHandler:)`](lineartimeseriesforecaster/model/applied(towindow:eventhandler:).md).

## Parameters

- `input`: An sequence of input features. Each feature’s shape must be  . If the sequence   contains less than   elements the method returns an empty array.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/applied(to:eventhandler:)-5kkin)*