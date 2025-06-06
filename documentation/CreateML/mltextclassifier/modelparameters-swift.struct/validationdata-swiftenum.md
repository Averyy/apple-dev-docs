# MLTextClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

The validation data that a text classifier uses.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum ValidationData
```

## Mentions

- [Creating a text classifier model](creating-a-text-classifier-model.md)

## Topics

### Specifying validation data
- [MLTextClassifier.ModelParameters.ValidationData.split(strategy:)](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generates the validation data by splitting the training dataset.
- [MLTextClassifier.ModelParameters.ValidationData.table(_:textColumn:labelColumn:)](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/table(_:textcolumn:labelcolumn:).md)
  Sets the validation data from the provided data table.
- [MLTextClassifier.ModelParameters.ValidationData.dataFrame(_:textColumn:labelColumn:)](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:textcolumn:labelcolumn:).md)
  Set validation data from the MLDataTable provided.
- [MLTextClassifier.ModelParameters.ValidationData.dataSource(_:)](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/datasource(_:).md)
  Sets the validation data from the provided data source.
- [MLTextClassifier.ModelParameters.ValidationData.dictionary(_:)](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/dictionary(_:).md)
  Sets the validation data from the provided dictionary.
- [MLTextClassifier.ModelParameters.ValidationData.none](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Doesn’t set validation data.

## See Also

- [init(validation: MLTextClassifier.ModelParameters.ValidationData, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](mltextclassifier/modelparameters-swift.struct/init(validation:algorithm:language:).md)
  Creates model parameters for a text classifier with the specified validation data, algorithm, and language.
- [struct NLLanguage](../NaturalLanguage/NLLanguage.md)
  The languages that the Natural Language framework supports.
- [MLTextClassifier.ModelAlgorithmType](mltextclassifier/modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum)*