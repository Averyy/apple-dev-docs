# MLSupportVectorClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

Values for specifying validation data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ValidationData
```

## Topics

### Specifying validation data
- [MLSupportVectorClassifier.ModelParameters.ValidationData.split(strategy:)](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.table(_:)](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.dataFrame(_:)](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Validation data provided in a DataFrame.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.none](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLSupportVectorClassifier.ModelParameters.ValidationData, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](mlsupportvectorclassifier/modelparameters-swift.struct/init(validation:maxiterations:penalty:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [init(validationData: MLDataTable?, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](mlsupportvectorclassifier/modelparameters-swift.struct/init(validationdata:maxiterations:penalty:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum)*