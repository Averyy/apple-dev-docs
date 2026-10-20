# MLLinearRegressor.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

Values for specifying validation data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ValidationData
```

## Topics

### Specifying validation data
- [MLLinearRegressor.ModelParameters.ValidationData.split(strategy:)](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLLinearRegressor.ModelParameters.ValidationData.table(_:)](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLLinearRegressor.ModelParameters.ValidationData.dataFrame(_:)](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Set validation data from the DataFrame provided.
- [MLLinearRegressor.ModelParameters.ValidationData.none](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLLinearRegressor.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [init(validationData: MLDataTable?, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum)*