# MLWordTagger.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The validation data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ValidationData
```

## Topics

### Specifying validation data
- [MLWordTagger.ModelParameters.ValidationData.split(strategy:)](./validationdata-swift.enum/split%28strategy%29.md)
  Generates the validation data by splitting the training dataset.
- [MLWordTagger.ModelParameters.ValidationData.table(_:tokenColumn:labelColumn:)](./validationdata-swift.enum/table%28_,tokencolumn,labelcolumn%29.md)
  Sets the validation data from the provided data table.
- [MLWordTagger.ModelParameters.ValidationData.dataFrame(_:tokenColumn:labelColumn:)](./validationdata-swift.enum/dataframe%28_,tokencolumn,labelcolumn%29.md)
  Set validation data from the DataFrame provided.
- [case tuples([(tokens: [MLWordTagger.Token], labels: [String])])](./validationdata-swift.enum/tuples%28_%29.md)
  Sets the validation data from a list of tokens and labels.
- [MLWordTagger.ModelParameters.ValidationData.none](./validationdata-swift.enum/none.md)
  Doesn’t set validation data.

## See Also

### Creating parameters
- [init(validation: MLWordTagger.ModelParameters.ValidationData, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](./init%28validation,algorithm,language%29.md)
  Creates model parameters.
- [MLWordTagger.ModelAlgorithmType](../modelalgorithmtype.md)
  The algorithm type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum)*