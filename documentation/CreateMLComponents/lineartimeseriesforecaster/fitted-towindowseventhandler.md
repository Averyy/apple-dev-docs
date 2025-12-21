# fitted(toWindows:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a model to a sequence of windows.

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
func fitted(toWindows input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws -> LinearTimeSeriesForecaster<Scalar>.Model
```

#### Return Value

The fitted model.

## Parameters

- `input`: A sequence of annotated windows. Each window’s shape should be    and each annotation’s shape should be  .
- `eventHandler`: An event handler.

## See Also

- [func update(inout LinearTimeSeriesForecaster<Scalar>.Transformer, with: AnnotatedBatch<Scalar>) async throws -> Scalar](lineartimeseriesforecaster/update(_:with:).md)
  Updates a model with a new batch of examples.
- [func update(inout LinearTimeSeriesForecaster<Scalar>.Model, withWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](lineartimeseriesforecaster/update(_:withwindows:eventhandler:).md)
  Updates a model with a sequence of windows.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(to:eventhandler:).md)
  Fits a model to a sequence of examples.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(to:validateon:eventhandler:).md)
  Fits a model to a sequence of examples with validation.
- [func fitted(toWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(towindows:validateon:eventhandler:).md)
  Fits a model to a sequence of annotated windows with validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/fitted(towindows:eventhandler:))*