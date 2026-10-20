# validationMetrics

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Measurements of the action classifier’s performance on the validation dataset.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var validationMetrics: MLClassifierMetrics { get }
```

## See Also

### Evaluating an action classifier
- [func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics](./evaluation%28on%29.md)
  Generates metrics describing the action classifier’s performance on labeled videos represented by a data source.
- [var trainingMetrics: MLClassifierMetrics](./trainingmetrics.md)
  Measurements of the action classifier’s performance on the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/validationmetrics)*