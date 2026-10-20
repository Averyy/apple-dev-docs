# MLSupportVectorClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

Values for specifying validation data.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
enum ValidationData
```

## Topics

### Specifying validation data
- [MLSupportVectorClassifier.ModelParameters.ValidationData.split(strategy:)](./validationdata-swift.enum/split%28strategy%29.md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.table(_:)](./validationdata-swift.enum/table%28_%29.md)
  Set validation data from the MLDataTable provided.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.dataFrame(_:)](./validationdata-swift.enum/dataframe%28_%29.md)
  Validation data provided in a DataFrame.
- [MLSupportVectorClassifier.ModelParameters.ValidationData.none](./validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

### Creating parameters
- [init(validation: MLSupportVectorClassifier.ModelParameters.ValidationData, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](./init%28validation,maxiterations,penalty,convergencethreshold,featurerescaling%29.md)
  Creates a new set of parameters.
- [init(validationData: MLDataTable?, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](./init%28validationdata,maxiterations,penalty,convergencethreshold,featurerescaling%29.md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum)*