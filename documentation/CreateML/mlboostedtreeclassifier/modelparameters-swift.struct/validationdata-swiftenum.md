# MLBoostedTreeClassifier.ModelParameters.ValidationData

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
- [MLBoostedTreeClassifier.ModelParameters.ValidationData.split(strategy:)](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLBoostedTreeClassifier.ModelParameters.ValidationData.table(_:)](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLBoostedTreeClassifier.ModelParameters.ValidationData.dataFrame(_:)](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Validation data provided in a DataFrame.
- [MLBoostedTreeClassifier.ModelParameters.ValidationData.none](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLBoostedTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters defining how a boosted tree classifier should be built.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum)*