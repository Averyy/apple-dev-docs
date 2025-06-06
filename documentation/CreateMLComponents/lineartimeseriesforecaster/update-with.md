# update(_:with:)

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
- watchOS 11.0+

## Declaration

```swift
func update(_ model: inout LinearTimeSeriesForecaster<Scalar>.Transformer, with input: AnnotatedBatch<Scalar>) async throws -> Scalar
```

#### Discussion

Use [`TimeSeriesForecasterBatches`](timeseriesforecasterbatches.md) to convert a shaped array of features into batches of windowed features and annotations. Here is an example of training a forecaster:

```None
let estimator = LinearTimeSeriesForecaster<Float>(configuration: configuration)
var model = estimator.makeTransformer()

let batches = try TimeSeriesForecasterBatches(
    features: features,       // shape [N, featureSize]
    annotations: annotations, // shape [N, annotationSize]
    batchSize: 32,
    inputWindowSize: configuration.inputWindowSize,
    forecastWindowSize: configuration.forecastWindowSize,
    shufflesBatches: true
)

for iteration in 0 ..< configuration.maximumIterationCount {
    for batch in batches {
        let loss = try await estimator.update(&model, with: batch)
        print("Loss: \(loss)")
    }
}
```

## Parameters

- `model`: The model to update.
- `input`: A shaped array of windowed features. The shape should be   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/update(_:with:))*