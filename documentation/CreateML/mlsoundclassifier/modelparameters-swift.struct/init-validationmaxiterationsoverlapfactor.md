# init(validation:maxIterations:overlapFactor:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of training parameters for a sound classifier with a validation dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLSoundClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), maxIterations: Int = 25, overlapFactor: Double = 0.5)
```

## Parameters

- `validation`: A validation dataset represented by an    instance.
- `maxIterations`: The largest number of iterations the training session can use to train the sound   classifier.
- `overlapFactor`: The default value is  , which represents a 50% overlap.

## See Also

- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset and a training algorithm.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType, featureExtractionTimeWindowSize: TimeInterval)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset, a training algorithm, and a time-window size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:))*