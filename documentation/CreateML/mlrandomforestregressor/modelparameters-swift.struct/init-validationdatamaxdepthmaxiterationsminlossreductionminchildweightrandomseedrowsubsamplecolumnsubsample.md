# init(validationData:maxDepth:maxIterations:minLossReduction:minChildWeight:randomSeed:rowSubsample:columnSubsample:)

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
init(validationData: MLDataTable? = nil, maxDepth: Int = 6, maxIterations: Int = 10, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42, rowSubsample: Double = 0.8, columnSubsample: Double = 0.8)
```

## Parameters

- `validationData`: The default value is   which will use an automatically sampled validation set.
- `maxDepth`: The default value is 6.
- `maxIterations`: The default value is 10.
- `minLossReduction`: The default value is 0.
- `minChildWeight`: The default value is 0.1.
- `randomSeed`: The default value is 42.
- `rowSubsample`: The default value is 0.8.
- `columnSubsample`: The default value is 0.8.

## See Also

- [init(validation: MLRandomForestRegressor.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestregressor/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
- [MLRandomForestRegressor.ModelParameters.ValidationData](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:))*