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

- `validation`: A validation dataset represented by an [`MLSoundClassifier.ModelParameters.ValidationData`](mlsoundclassifier/modelparameters-swift.struct/validationdata.md) instance.
- `maxIterations`: The largest number of iterations the training session can use to train the sound classifier.
- `overlapFactor`: A proportion of overlap the training session uses to analyze two consecutive windows in the audio data. The proportion must be in the range `[0.0, 1.0)`. Higher proportions generate more training data, but also increases the training time. The default value is `0.5`, which represents a 50% overlap.

## See Also

- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset and a training algorithm.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType, featureExtractionTimeWindowSize: TimeInterval)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset, a training algorithm, and a time-window size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:))*