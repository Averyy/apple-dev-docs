# MLTextClassifier.ModelParameters.ValidationData.dataSource(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Sets the validation data from the provided data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case dataSource(MLTextClassifier.DataSource)
```

## See Also

### Specifying validation data
- [MLTextClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  Generates the validation data by splitting the training dataset.
- [MLTextClassifier.ModelParameters.ValidationData.table(_:textColumn:labelColumn:)](./table%28_,textcolumn,labelcolumn%29.md)
  Sets the validation data from the provided data table.
- [MLTextClassifier.ModelParameters.ValidationData.dataFrame(_:textColumn:labelColumn:)](./dataframe%28_,textcolumn,labelcolumn%29.md)
  Set validation data from the MLDataTable provided.
- [MLTextClassifier.ModelParameters.ValidationData.dictionary(_:)](./dictionary%28_%29.md)
  Sets the validation data from the provided dictionary.
- [MLTextClassifier.ModelParameters.ValidationData.none](./none.md)
  Doesn’t set validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/datasource(_:))*