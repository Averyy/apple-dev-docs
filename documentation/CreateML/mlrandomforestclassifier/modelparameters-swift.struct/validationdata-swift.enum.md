# MLRandomForestClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLRandomForestClassifier.ModelParameters.ValidationData.split(strategy:)](./validationdata-swift.enum/split%28strategy%29.md)
  Generate validation data by splitting the training dataset. This is the default.
- [MLRandomForestClassifier.ModelParameters.ValidationData.table(_:)](./validationdata-swift.enum/table%28_%29.md)
  Set validation data from the MLDataTable provided.
- [MLRandomForestClassifier.ModelParameters.ValidationData.dataFrame(_:)](./validationdata-swift.enum/dataframe%28_%29.md)
  Validation data provided in a DataFrame.
- [MLRandomForestClassifier.ModelParameters.ValidationData.none](./validationdata-swift.enum/none.md)
  Do not set validation data.

## See Also

### Creating parameters
- [init(validation: MLRandomForestClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](./init%28validation,maxdepth,maxiterations,minlossreduction,minchildweight,randomseed,rowsubsample,columnsubsample%29.md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](./init%28validationdata,maxdepth,maxiterations,minlossreduction,minchildweight,randomseed,rowsubsample,columnsubsample%29.md)
  Creates a new set of parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.enum)*