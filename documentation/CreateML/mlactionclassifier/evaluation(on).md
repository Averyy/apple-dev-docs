# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics describing the action classifier’s performance on labeled videos represented by a data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func evaluation(on annotatedVideos: MLActionClassifier.DataSource) throws -> MLClassifierMetrics
```

## Parameters

- `annotatedVideos`: A collection of labeled videos represented by a data source.

## See Also

### Evaluating an action classifier
- [var trainingMetrics: MLClassifierMetrics](./trainingmetrics.md)
  Measurements of the action classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](./validationmetrics.md)
  Measurements of the action classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/evaluation(on:))*