# init(validationData:maxDepth:maxIterations:minLossReduction:minChildWeight:randomSeed:stepSize:earlyStoppingRounds:rowSubsample:columnSubsample:)

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
init(validationData: MLDataTable? = nil, maxDepth: Int = 6, maxIterations: Int = 10, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42, stepSize: Double = 0.3, earlyStoppingRounds: Int? = nil, rowSubsample: Double = 1.0, columnSubsample: Double = 1.0)
```

## Parameters

- `validationData`: The dataset used to monitor how well the model is generalizing. The default value is `nil` which will use an automatically sampled validation set.
- `maxDepth`: The maximum depth of the tree. Must be a value of at least 1. The default value is 6.
- `maxIterations`: The maximum number of passes through the data. Each iteration creates an extra tree. The default value is 10.
- `minLossReduction`: The minimum amount of reduction in the loss function that is required to make another split to the data. Larger values help prevent overfitting. The default value is 0.
- `minChildWeight`: Determines the minimum weight of each leaf node of the tree. Larger values help prevent overfitting. The default value is 0.1.
- `randomSeed`: A seed for internal random operations. Set this value to ensure reproducible results. The default value is 42.
- `stepSize`: The size used to decrease the prediction weight of each learner. The smaller the step size the more conservative the boosting process will be. The default value is 0.3.
- `earlyStoppingRounds`: If the validation accuracy does not improve after the specified number of rounds training will stop.
- `rowSubsample`: Select the specified ratio from the training set to grow each tree. For example, a value of 0.5 means each tree is trained on half the data. This technique is known as *bagging*. The default value is 1.0.
- `columnSubsample`: Select the specified ratio of columns from the training set to use when growing each tree. Similar to row subsampling, this can be used to prevent overfitting. The default value is 1.0.

## See Also

- [init(validation: MLBoostedTreeRegressor.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeregressor/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
- [MLBoostedTreeRegressor.ModelParameters.ValidationData](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:))*