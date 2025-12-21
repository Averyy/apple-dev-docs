# update(_:withWindows:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a model with a sequence of windows.

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
func update(_ model: inout LinearTimeSeriesForecaster<Scalar>.Model, withWindows windows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler? = nil) async throws
```

#### Discussion

For faster updates, consider passing a single [`AnnotatedBatch`](annotatedbatch.md) with shaped arrays that contain multiple training examples. See [`update(_:with:)`](lineartimeseriesforecaster/update(_:with:).md).

## Parameters

- `model`: The model to update.
- `windows`: A sequence of annotated windows. The feature shape must be   and   the annotation shape must be  .
- `eventHandler`: An event handler.

## See Also

- [func update(inout LinearTimeSeriesForecaster<Scalar>.Transformer, with: AnnotatedBatch<Scalar>) async throws -> Scalar](lineartimeseriesforecaster/update(_:with:).md)
  Updates a model with a new batch of examples.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(to:eventhandler:).md)
  Fits a model to a sequence of examples.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(to:validateon:eventhandler:).md)
  Fits a model to a sequence of examples with validation.
- [func fitted(toWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(towindows:eventhandler:).md)
  Fits a model to a sequence of windows.
- [func fitted(toWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/fitted(towindows:validateon:eventhandler:).md)
  Fits a model to a sequence of annotated windows with validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/update(_:withwindows:eventhandler:))*