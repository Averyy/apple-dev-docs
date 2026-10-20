# init(validation:maxDepth:maxIterations:minLossReduction:minChildWeight:randomSeed:stepSize:earlyStoppingRounds:rowSubsample:columnSubsample:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLBoostedTreeClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), maxDepth: Int = 6, maxIterations: Int = 10, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42, stepSize: Double = 0.3, earlyStoppingRounds: Int? = nil, rowSubsample: Double = 1.0, columnSubsample: Double = 1.0)
```

## See Also

### Creating parameters
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](./init%28validationdata,maxdepth,maxiterations,minlossreduction,minchildweight,randomseed,stepsize,earlystoppingrounds,rowsubsample,columnsubsample%29.md)
  Creates a new set of parameters defining how a boosted tree classifier should be built.
- [MLBoostedTreeClassifier.ModelParameters.ValidationData](./validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:))*