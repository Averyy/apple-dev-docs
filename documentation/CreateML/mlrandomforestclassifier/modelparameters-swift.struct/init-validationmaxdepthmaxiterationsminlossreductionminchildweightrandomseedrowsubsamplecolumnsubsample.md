# init(validation:maxDepth:maxIterations:minLossReduction:minChildWeight:randomSeed:rowSubsample:columnSubsample:)

**Framework**: Create ML  
**Kind**: init

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLRandomForestClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), maxDepth: Int = 6, maxIterations: Int = 10, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42, rowSubsample: Double = 0.8, columnSubsample: Double = 0.8)
```

## See Also

- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters.
- [MLRandomForestClassifier.ModelParameters.ValidationData](mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:))*