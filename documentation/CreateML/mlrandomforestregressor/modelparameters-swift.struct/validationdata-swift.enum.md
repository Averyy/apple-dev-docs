# MLRandomForestRegressor.ModelParameters.ValidationData

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
- [MLRandomForestRegressor.ModelParameters.ValidationData.split(strategy:)](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLRandomForestRegressor.ModelParameters.ValidationData.table(_:)](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLRandomForestRegressor.ModelParameters.ValidationData.dataFrame(_:)](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Set validation data from the DataFrame provided.
- [MLRandomForestRegressor.ModelParameters.ValidationData.none](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLRandomForestRegressor.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestregressor/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestregressor/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum)*