# MLWordTagger.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Generates the validation data by splitting the training dataset.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

#### Discussion

By default, model parameters use this approach to specify the validation data.

## See Also

### Specifying validation data
- [MLWordTagger.ModelParameters.ValidationData.table(_:tokenColumn:labelColumn:)](./table%28_,tokencolumn,labelcolumn%29.md)
  Sets the validation data from the provided data table.
- [MLWordTagger.ModelParameters.ValidationData.dataFrame(_:tokenColumn:labelColumn:)](./dataframe%28_,tokencolumn,labelcolumn%29.md)
  Set validation data from the DataFrame provided.
- [case tuples([(tokens: [MLWordTagger.Token], labels: [String])])](./tuples%28_%29.md)
  Sets the validation data from a list of tokens and labels.
- [MLWordTagger.ModelParameters.ValidationData.none](./none.md)
  Doesn’t set validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:))*