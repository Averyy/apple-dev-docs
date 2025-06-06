# MLWordTagger.ModelParameters.ValidationData.tuples(_:)

**Framework**: Create ML  
**Kind**: case

Sets the validation data from a list of tokens and labels.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case tuples([(tokens: [MLWordTagger.Token], labels: [String])])
```

## See Also

- [MLWordTagger.ModelParameters.ValidationData.split(strategy:)](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generates the validation data by splitting the training dataset.
- [MLWordTagger.ModelParameters.ValidationData.table(_:tokenColumn:labelColumn:)](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/table(_:tokencolumn:labelcolumn:).md)
  Sets the validation data from the provided data table.
- [MLWordTagger.ModelParameters.ValidationData.dataFrame(_:tokenColumn:labelColumn:)](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:tokencolumn:labelcolumn:).md)
  Set validation data from the DataFrame provided.
- [MLWordTagger.ModelParameters.ValidationData.none](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Doesn’t set validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/tuples(_:))*