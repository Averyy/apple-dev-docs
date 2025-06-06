# MLWordTagger.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

The validation data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ValidationData
```

## Topics

### Specifying validation data
- [MLWordTagger.ModelParameters.ValidationData.split(strategy:)](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generates the validation data by splitting the training dataset.
- [MLWordTagger.ModelParameters.ValidationData.table(_:tokenColumn:labelColumn:)](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/table(_:tokencolumn:labelcolumn:).md)
  Sets the validation data from the provided data table.
- [MLWordTagger.ModelParameters.ValidationData.dataFrame(_:tokenColumn:labelColumn:)](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:tokencolumn:labelcolumn:).md)
  Set validation data from the DataFrame provided.
- [case tuples([(tokens: [MLWordTagger.Token], labels: [String])])](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/tuples(_:).md)
  Sets the validation data from a list of tokens and labels.
- [MLWordTagger.ModelParameters.ValidationData.none](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Doesn’t set validation data.

## See Also

- [init(validation: MLWordTagger.ModelParameters.ValidationData, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](mlwordtagger/modelparameters-swift.struct/init(validation:algorithm:language:).md)
  Creates model parameters.
- [MLWordTagger.ModelAlgorithmType](mlwordtagger/modelalgorithmtype.md)
  The algorithm type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum)*