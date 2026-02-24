# init(validation:maxIterations:penalty:convergenceThreshold:featureRescaling:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of parameters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(validation: MLSupportVectorClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), maxIterations: Int = 11, penalty: Double = 1.0, convergenceThreshold: Double = 0.01, featureRescaling: Bool = true)
```

## Parameters

- `validation`: The data used to monitor how well the model is generalizing. The default is to automatically split off some data from the training set for validation.
- `maxIterations`: The maximum number of passes through the data. The default value is 11.
- `penalty`: Weight of the regularizer. The larger the penalty the less variance in the model. The default value is 1.0.
- `convergenceThreshold`: The threshold with which to determine if the model has converged. Consider reducing this value for higher training accuracy, but beware of overfitting. The default value is 0.01.
- `featureRescaling`: Determines if the features should be preprocessed to ensure all features are on the same scale. The default value is true.

## See Also

- [init(validationData: MLDataTable?, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](mlsupportvectorclassifier/modelparameters-swift.struct/init(validationdata:maxiterations:penalty:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [MLSupportVectorClassifier.ModelParameters.ValidationData](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/init(validation:maxiterations:penalty:convergencethreshold:featurerescaling:))*