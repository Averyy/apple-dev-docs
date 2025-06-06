# validationMetrics

**Framework**: Create ML  
**Kind**: property

Measurements of the action classifier’s performance on the validation dataset.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var validationMetrics: MLClassifierMetrics { get }
```

## See Also

- [var trainingMetrics: MLClassifierMetrics](mlactionclassifier/trainingmetrics.md)
  Measurements of the action classifier’s performance on the training dataset.
- [func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics](mlactionclassifier/evaluation(on:).md)
  Generates metrics describing the action classifier’s performance on labeled videos represented by a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics)*