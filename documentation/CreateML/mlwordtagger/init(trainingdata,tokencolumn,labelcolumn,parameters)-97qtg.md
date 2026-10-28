# init(trainingData:tokenColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a word tagger.

**Availability**:
- macOS 10.14+ - Deprecated in 13.0

> **Deprecated**: Use DataFrame instead of MLDataTable when initializing.

## Declaration

```swift
init(trainingData: MLDataTable, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters = ModelParameters(validationData: nil)) throws
```

**Other overloads**:

```swift
init(trainingData: DataFrame, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: A table specifying training data.
- `tokenColumn`: The name of the token column in the training data frame.
- `labelColumn`: The name of the label column in the training data frame.
- `parameters`: The model parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:)-97qtg)*