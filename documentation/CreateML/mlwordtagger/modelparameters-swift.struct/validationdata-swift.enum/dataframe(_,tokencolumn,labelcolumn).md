# MLWordTagger.ModelParameters.ValidationData.dataFrame(_:tokenColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Set validation data from the DataFrame provided.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case dataFrame(DataFrame, tokenColumn: String, labelColumn: String)
```

## See Also

### Specifying validation data
- [MLWordTagger.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  Generates the validation data by splitting the training dataset.
- [MLWordTagger.ModelParameters.ValidationData.table(_:tokenColumn:labelColumn:)](./table%28_,tokencolumn,labelcolumn%29.md)
  Sets the validation data from the provided data table.
- [case tuples([(tokens: [MLWordTagger.Token], labels: [String])])](./tuples%28_%29.md)
  Sets the validation data from a list of tokens and labels.
- [MLWordTagger.ModelParameters.ValidationData.none](./none.md)
  Doesn’t set validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:tokencolumn:labelcolumn:))*