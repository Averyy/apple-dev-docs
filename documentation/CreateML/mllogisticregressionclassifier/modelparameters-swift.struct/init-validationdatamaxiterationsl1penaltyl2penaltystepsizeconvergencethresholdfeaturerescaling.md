# init(validationData:maxIterations:l1Penalty:l2Penalty:stepSize:convergenceThreshold:featureRescaling:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(validationData: MLDataTable?, maxIterations: Int = 10, l1Penalty: Double = 0, l2Penalty: Double = 0.01, stepSize: Double = 1.0, convergenceThreshold: Double = 0.01, featureRescaling: Bool = true)
```

## Parameters

- `validationData`: The default value is   which will use an automatically sampled validation set.
- `maxIterations`: The default value is 10.
- `l1Penalty`: The default value is 0 which prevents any values from being discarded.
- `l2Penalty`: The default value is 0.01.
- `stepSize`: The default value is 1.0.
- `convergenceThreshold`: The default value is 0.01.
- `featureRescaling`: The default value is true.

## See Also

- [init(validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllogisticregressionclassifier/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [MLLogisticRegressionClassifier.ModelParameters.ValidationData](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:))*