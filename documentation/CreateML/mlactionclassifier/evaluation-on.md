# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics describing the action classifier’s performance on labeled videos represented by a data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func evaluation(on annotatedVideos: MLActionClassifier.DataSource) throws -> MLClassifierMetrics
```

#### Discussion

- annotatedVideos: A collection of labeled videos represented by a data source.

## See Also

- [var trainingMetrics: MLClassifierMetrics](mlactionclassifier/trainingmetrics.md)
  Measurements of the action classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlactionclassifier/validationmetrics.md)
  Measurements of the action classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/evaluation(on:))*