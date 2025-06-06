# MLBoostedTreeRegressor.ModelParameters.ValidationData

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
- [MLBoostedTreeRegressor.ModelParameters.ValidationData.split(strategy:)](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLBoostedTreeRegressor.ModelParameters.ValidationData.table(_:)](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLBoostedTreeRegressor.ModelParameters.ValidationData.dataFrame(_:)](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Set validation data from the DataFrame provided.
- [MLBoostedTreeRegressor.ModelParameters.ValidationData.none](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLBoostedTreeRegressor.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeregressor/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeregressor/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum)*