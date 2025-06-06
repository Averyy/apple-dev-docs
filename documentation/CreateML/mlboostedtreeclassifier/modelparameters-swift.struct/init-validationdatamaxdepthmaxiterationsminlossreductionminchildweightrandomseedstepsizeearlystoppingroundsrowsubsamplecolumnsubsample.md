# init(validationData:maxDepth:maxIterations:minLossReduction:minChildWeight:randomSeed:stepSize:earlyStoppingRounds:rowSubsample:columnSubsample:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of parameters defining how a boosted tree classifier should be built.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(validationData: MLDataTable?, maxDepth: Int = 6, maxIterations: Int = 10, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42, stepSize: Double = 0.3, earlyStoppingRounds: Int? = nil, rowSubsample: Double = 1.0, columnSubsample: Double = 1.0)
```

## Parameters

- `validationData`: The default value is   which will use an automatically sampled validation set.
- `maxDepth`: The default value is 6.
- `maxIterations`: The default value is 10.
- `minLossReduction`: The default value is 0.
- `minChildWeight`: The default value is 0.1.
- `randomSeed`: The default value is 42.
- `stepSize`: The default value is 0.3.
- `earlyStoppingRounds`: If the validation accuracy does not improve after the specified number of rounds   training will stop.
- `rowSubsample`: The default value is 1.0.
- `columnSubsample`: The default value is 1.0.

## See Also

- [init(validation: MLBoostedTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
- [MLBoostedTreeClassifier.ModelParameters.ValidationData](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:))*