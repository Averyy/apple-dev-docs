# MLTextClassifier.ModelParameters.ValidationData.dataFrame(_:textColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Set validation data from the MLDataTable provided.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case dataFrame(DataFrame, textColumn: String, labelColumn: String)
```

## See Also

### Specifying validation data
- [MLTextClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  Generates the validation data by splitting the training dataset.
- [MLTextClassifier.ModelParameters.ValidationData.table(_:textColumn:labelColumn:)](./table%28_,textcolumn,labelcolumn%29.md)
  Sets the validation data from the provided data table.
- [MLTextClassifier.ModelParameters.ValidationData.dataSource(_:)](./datasource%28_%29.md)
  Sets the validation data from the provided data source.
- [MLTextClassifier.ModelParameters.ValidationData.dictionary(_:)](./dictionary%28_%29.md)
  Sets the validation data from the provided dictionary.
- [MLTextClassifier.ModelParameters.ValidationData.none](./none.md)
  Doesn’t set validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:textcolumn:labelcolumn:))*