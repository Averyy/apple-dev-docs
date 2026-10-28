# MLSoundClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

Parameters that affect the process of training a sound-classifier model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

## Overview

By default, a sound-classifier training session’s transfer-learning algorithm uses the [`MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)`](./modelparameters-swift.struct/featureextractortype/audiofeatureprint%28type,revision%29.md) feature extractor. See [`MLSoundClassifier.ModelParameters.FeatureExtractorType`](./modelparameters-swift.struct/featureextractortype.md) for more information.

## Topics

### Creating parameters
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double)](./modelparameters-swift.struct/init%28validation,maxiterations,overlapfactor%29.md)
  Creates a new set of training parameters for a sound classifier with a validation dataset.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)](./modelparameters-swift.struct/init%28validation,maxiterations,overlapfactor,algorithm%29.md)
  Creates a new set of training parameters for a sound classifier with a validation dataset and a training algorithm.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType, featureExtractionTimeWindowSize: TimeInterval)](./modelparameters-swift.struct/init%28validation,maxiterations,overlapfactor,algorithm,featureextractiontimewindowsize%29.md)
  Creates a new set of training parameters for a sound classifier with a validation dataset, a training algorithm, and a time-window size.
### Accessing the training parameters
- [var validation: MLSoundClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  The sound classifier’s validation dataset.
- [var maxIterations: Int](./modelparameters-swift.struct/maxiterations.md)
  The largest number of iterations the training session can use.
- [var overlapFactor: Double](./modelparameters-swift.struct/overlapfactor.md)
  The proportion of overlap that the training session uses to analyze two consecutive windows in the audio data.
- [var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType](./modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the sound classifier.
- [var featureExtractionTimeWindowSize: TimeInterval](./modelparameters-swift.struct/featureextractiontimewindowsize.md)
  A time duration, in seconds, the training session uses for each audio sample it reads from an audio file in a dataset.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the parameters in a playground.
### Supporting types
- [MLSoundClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for a sound classifier.
- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](./modelparameters-swift.struct/modelalgorithmtype.md)
  The algorithm options to train a sound classifier.
- [MLSoundClassifier.ModelParameters.ClassifierType](./modelparameters-swift.struct/classifiertype.md)
  The classifier options for a sound classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType](./modelparameters-swift.struct/featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](./modelparameters-swift.struct/featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Supporting types
- [MLSoundClassifier.DataSource](./datasource.md)
  A representation of a sound-classifier dataset located in the file system or in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)*