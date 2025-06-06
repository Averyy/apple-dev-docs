# MLTextClassifier.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case

Generates the validation data by splitting the training dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

#### Discussion

By default, model parameters use this approach to specify the validation data.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:))*