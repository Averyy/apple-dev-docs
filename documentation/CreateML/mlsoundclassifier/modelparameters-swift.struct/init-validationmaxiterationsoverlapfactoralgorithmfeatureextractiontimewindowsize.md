# init(validation:maxIterations:overlapFactor:algorithm:featureExtractionTimeWindowSize:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of training parameters for a sound classifier with a validation dataset, a training algorithm, and a time-window size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLSoundClassifier.ModelParameters.ValidationData = __Defaults.validation, maxIterations: Int = __Defaults.maximumIterations, overlapFactor: Double = __Defaults.overlapFactor, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType = __Defaults.algorithm, featureExtractionTimeWindowSize: TimeInterval = __Defaults.defaultVGGishTimeWindow)
```

## Parameters

- `validation`: A validation dataset represented by an    instance.
- `maxIterations`: The largest number of iterations the training session can use to train the sound   classifier.
- `overlapFactor`: The default value is  , which represents a 50% overlap.
- `algorithm`: An algorithm the training session uses to train the sound classifier.
- `featureExtractionTimeWindowSize`: A time duration, in seconds, the feature-extraction session uses for   each audio sample it reads from an audio file in a dataset. The value must be in the range   .

## See Also

- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset and a training algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:))*