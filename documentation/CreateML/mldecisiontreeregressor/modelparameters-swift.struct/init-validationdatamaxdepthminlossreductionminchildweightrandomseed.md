# init(validationData:maxDepth:minLossReduction:minChildWeight:randomSeed:)

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
init(validationData: MLDataTable? = nil, maxDepth: Int = 6, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42)
```

## Parameters

- `validationData`: The default value is   which will use an automatically sampled validation set.
- `maxDepth`: The default value is 6.
- `minLossReduction`: The default value is 0.
- `minChildWeight`: The default value is 0.1.
- `randomSeed`: The default value is 42.

## See Also

- [init(validation: MLDecisionTreeRegressor.ModelParameters.ValidationData, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeregressor/modelparameters-swift.struct/init(validation:maxdepth:minlossreduction:minchildweight:randomseed:).md)
- [MLDecisionTreeRegressor.ModelParameters.ValidationData](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/modelparameters-swift.struct/init(validationdata:maxdepth:minlossreduction:minchildweight:randomseed:))*