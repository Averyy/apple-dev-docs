# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a model with a new batch of examples.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func update(_ transformer: inout TimeSeriesClassifier<Scalar, Label>.Model, with input: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler? = nil) async throws
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of annotated features for updating the transformer. Each feature’s shape should be   .
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/update(_:with:eventhandler:))*