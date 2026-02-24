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
init(validationData: MLDataTable? = nil, maxIterations: Int = 10, l1Penalty: Double = 0, l2Penalty: Double = 0.01, stepSize: Double = 1.0, convergenceThreshold: Double = 0.01, featureRescaling: Bool = true)
```

## Parameters

- `validationData`: The dataset used to monitor how well the model is generalizing. The default value is `nil` which will use an automatically sampled validation set.
- `maxIterations`: The maximum number of passes through the data. The default value is 10.
- `l1Penalty`: Weight on the l1-regularizer. The l1Penalty zeros out small coefficients, indicating features that are not useful for the  model. The default value is 0 which prevents any values from being discarded.
- `l2Penalty`: Weight of the l2-regularizer. The larger the l2Penalty the less variance in the model. The default value is 0.01.
- `stepSize`: The adjustment size that should be made by the underlying solver. Values close to 1.0 take an aggressive step based off feedback from each training iteration. The default value is 1.0.
- `convergenceThreshold`: The threshold with which to determine if the model has converged. Consider reducing this value for higher training accuracy, but beware of overfitting. The default value is 0.01.
- `featureRescaling`: Determines if the features should be preprocessed to ensure all features are on the same scale. The default value is true.

## See Also

- [init(validation: MLLinearRegressor.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [MLLinearRegressor.ModelParameters.ValidationData](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:))*