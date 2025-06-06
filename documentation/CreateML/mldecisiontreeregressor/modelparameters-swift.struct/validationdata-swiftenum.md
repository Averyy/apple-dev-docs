# MLDecisionTreeRegressor.ModelParameters.ValidationData

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
- [MLDecisionTreeRegressor.ModelParameters.ValidationData.split(strategy:)](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLDecisionTreeRegressor.ModelParameters.ValidationData.table(_:)](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum/table(_:).md)
  Set validation data from the MLDataTable provided.
- [MLDecisionTreeRegressor.ModelParameters.ValidationData.dataFrame(_:)](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum/dataframe(_:).md)
  Set validation data from the DataFrame provided.
- [MLDecisionTreeRegressor.ModelParameters.ValidationData.none](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

- [init(validation: MLDecisionTreeRegressor.ModelParameters.ValidationData, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeregressor/modelparameters-swift.struct/init(validation:maxdepth:minlossreduction:minchildweight:randomseed:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeregressor/modelparameters-swift.struct/init(validationdata:maxdepth:minlossreduction:minchildweight:randomseed:).md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum)*