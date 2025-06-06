# fitted(toWindows:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a model to a sequence of annotated windows with validation.

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
func fitted(toWindows input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn validation: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws -> LinearTimeSeriesForecaster<Scalar>.Model
```

#### Return Value

The fitted model.

## Parameters

- `input`: A sequence of annotated windows. Each window’s shape should be    and each annotation’s shape should be  .
- `validation`: A sequence of annotated validation windows. The feature and annotation shapes should be the   same as the input parameter.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/fitted(towindows:validateon:eventhandler:))*