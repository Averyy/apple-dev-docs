# trainingMetrics

**Framework**: Create ML  
**Kind**: property

Measurements of the action classifier’s performance on the training dataset.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var trainingMetrics: MLClassifierMetrics { get }
```

## See Also

- [var validationMetrics: MLClassifierMetrics](mlactionclassifier/validationmetrics.md)
  Measurements of the action classifier’s performance on the validation dataset.
- [func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics](mlactionclassifier/evaluation(on:).md)
  Generates metrics describing the action classifier’s performance on labeled videos represented by a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/trainingmetrics)*