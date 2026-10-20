# MLSupportVectorClassifier.ModelParameters.ValidationData.table(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Set validation data from the MLDataTable provided.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
case table(MLDataTable)
```

## See Also

### Specifying validation data
- [MLSupportVectorClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.dataFrame(_:)](./dataframe%28_%29.md)
  Validation data provided in a DataFrame.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.none](./none.md)
  Do not set validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum/table(_:))*