# prediction(from:options:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Predicts output values from the given input features.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

```objc
- (id<MLFeatureProvider>) predictionFromFeatures:(id<MLFeatureProvider>) input options:(MLPredictionOptions *) options error:(NSError **) error;
```

## Return Value

A feature provider that represents the model’s prediction.

## Parameters

- `input`: The feature values the models needs to make its prediction.
- `options`: The options to be applied to the prediction.

## See Also

### Making predictions
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](./predictions%28from,options%29.md)
  Predicts output values from the given batch of input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustommodel/prediction(from:options:))*