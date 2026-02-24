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

- `validation`: A validation dataset represented by an [`MLSoundClassifier.ModelParameters.ValidationData`](mlsoundclassifier/modelparameters-swift.struct/validationdata.md) instance.
- `maxIterations`: The largest number of iterations the training session can use to train the sound classifier.
- `overlapFactor`: A proportion of overlap the training session uses to analyze two consecutive windows in the audio data. The proportion must be in the range `[0.0, 1.0)`. Higher proportions generate more training data but also increase the training time. The default value is `0.5`, which represents a 50% overlap.
- `algorithm`: An algorithm the training session uses to train the sound classifier.
- `featureExtractionTimeWindowSize`: A time duration, in seconds, the feature-extraction session uses for each audio sample it reads from an audio file in a dataset. The value must be in the range `[0.5, 15.0]`.

## See Also

- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset and a training algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:))*