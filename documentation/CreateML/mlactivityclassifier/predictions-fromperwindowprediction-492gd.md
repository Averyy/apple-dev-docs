# predictions(from:perWindowPrediction:)

**Framework**: Create ML  
**Kind**: method

Predict activities from new observations.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func predictions(from data: DataFrame, perWindowPrediction: Bool? = false) throws -> [String]
```

#### Return Value

An array of predicted class names.

#### Discussion

- Parameters - testingData: A data frame containing unlabeled sensor data samples. All samples are assumed to come from the same recording. Feature column names used in the table should be consistent with those used in training.
- perWindowPrediction: A Boolean option to specify the prediction frequency. Default is false, and prediction is made per sample, instead of per window.

> **Note**: `MLCreateError.type` if `testingData` format is invalid.

## See Also

- [func predictions(from: MLDataTable, perWindowPrediction: Bool?) throws -> [String]](mlactivityclassifier/predictions(from:perwindowprediction:)-6tatv.md)
  Predict activities from new observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/predictions(from:perwindowprediction:)-492gd)*