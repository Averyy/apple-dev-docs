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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/update(_:withwindows:eventhandler:))*