# init(trainingData:textColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a text classifier.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable when initializing.

## Declaration

```swift
init(trainingData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

**Other overloads**:

```swift
init(trainingData: DataFrame, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: A table specifying training data
- `textColumn`: Name of the text column in the provided trainingData
- `labelColumn`: Name of the label column in the provided trainingData
- `parameters`: Model training parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-7lp6w)*