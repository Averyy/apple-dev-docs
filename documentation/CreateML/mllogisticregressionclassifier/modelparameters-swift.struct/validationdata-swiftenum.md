# MLLogisticRegressionClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

Values for specifying validation data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ValidationData
```

## Topics

### Specifying validation data
- [MLLogisticRegressionClassifier.ModelParameters.ValidationData.split(strategy:)](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLLogisticRegressionClassifier.ModelParameters.ValidationData.table(_:)](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLLogisticRegressionClassifier.ModelParameters.ValidationData.dataFrame(_:)](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Validation data provided in a DataFrame.
- [MLLogisticRegressionClassifier.ModelParameters.ValidationData.none](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllogisticregressionclassifier/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [init(validationData: MLDataTable?, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllogisticregressionclassifier/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum)*