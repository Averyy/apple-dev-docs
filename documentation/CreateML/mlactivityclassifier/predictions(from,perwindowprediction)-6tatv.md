# predictions(from:perWindowPrediction:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predict activities from new observations.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func predictions(from data: MLDataTable, perWindowPrediction: Bool? = false) throws -> [String]
```

**Other overloads**:

```swift
func predictions(from data: DataFrame, perWindowPrediction: Bool? = false) throws -> [String]
```

## Return Value

An array of predicted class names.

## Discussion

> **Throws**: `MLCreateError.type` if `testingData` format is invalid.

## Parameters

- `data`: A MLDataTable containing unlabeled sensor data samples. All samples are assumed to come from the same recording. Feature column names used in the table should be consistent with those used in training.
- `perWindowPrediction`: A Boolean option to specify the prediction frequency. Default is false, and prediction is made per sample, instead of per window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/predictions(from:perwindowprediction:)-6tatv)*