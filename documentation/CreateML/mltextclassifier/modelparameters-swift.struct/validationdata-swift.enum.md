# MLTextClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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

- [Creating a text classifier model](../../creating-a-text-classifier-model.md)

## Topics

### Specifying validation data
- [MLTextClassifier.ModelParameters.ValidationData.split(strategy:)](./validationdata-swift.enum/split%28strategy%29.md)
  Generates the validation data by splitting the training dataset.
- [MLTextClassifier.ModelParameters.ValidationData.table(_:textColumn:labelColumn:)](./validationdata-swift.enum/table%28_,textcolumn,labelcolumn%29.md)
  Sets the validation data from the provided data table.
- [MLTextClassifier.ModelParameters.ValidationData.dataFrame(_:textColumn:labelColumn:)](./validationdata-swift.enum/dataframe%28_,textcolumn,labelcolumn%29.md)
  Set validation data from the MLDataTable provided.
- [MLTextClassifier.ModelParameters.ValidationData.dataSource(_:)](./validationdata-swift.enum/datasource%28_%29.md)
  Sets the validation data from the provided data source.
- [MLTextClassifier.ModelParameters.ValidationData.dictionary(_:)](./validationdata-swift.enum/dictionary%28_%29.md)
  Sets the validation data from the provided dictionary.
- [MLTextClassifier.ModelParameters.ValidationData.none](./validationdata-swift.enum/none.md)
  Doesn’t set validation data.

## See Also

### Creating parameters
- [init(validation: MLTextClassifier.ModelParameters.ValidationData, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](./init%28validation,algorithm,language%29.md)
  Creates model parameters for a text classifier with the specified validation data, algorithm, and language.
- [struct NLLanguage](../../../NaturalLanguage/nllanguage.md)
  The languages that the Natural Language framework supports.
- [MLTextClassifier.ModelAlgorithmType](../modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum)*