# MLSoundClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

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

#### Overview

By default, a sound-classifier training session’s transfer-learning algorithm uses the [`MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)`](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:).md) feature extractor. See [`MLSoundClassifier.ModelParameters.FeatureExtractorType`](mlsoundclassifier/modelparameters-swift.struct/featureextractortype.md) for more information.

## Topics

### Creating parameters
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset and a training algorithm.
- [init(validation: MLSoundClassifier.ModelParameters.ValidationData, maxIterations: Int, overlapFactor: Double, algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType, featureExtractionTimeWindowSize: TimeInterval)](mlsoundclassifier/modelparameters-swift.struct/init(validation:maxiterations:overlapfactor:algorithm:featureextractiontimewindowsize:).md)
  Creates a new set of training parameters for a sound classifier with a validation dataset, a training algorithm, and a time-window size.
### Accessing the training parameters
- [var validation: MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validation.md)
  The sound classifier’s validation dataset.
- [var maxIterations: Int](mlsoundclassifier/modelparameters-swift.struct/maxiterations.md)
  The largest number of iterations the training session can use.
- [var overlapFactor: Double](mlsoundclassifier/modelparameters-swift.struct/overlapfactor.md)
  The proportion of overlap that the training session uses to analyze two consecutive windows in the audio data.
- [var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType](mlsoundclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the sound classifier.
- [var featureExtractionTimeWindowSize: TimeInterval](mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize.md)
  A time duration, in seconds, the training session uses for each audio sample it reads from an audio file in a dataset.
### Describing parameters
- [var description: String](mlsoundclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mlsoundclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlsoundclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the parameters in a playground.
### Supporting types
- [MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for a sound classifier.
- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The algorithm options to train a sound classifier.
### Enumerations
- [MLSoundClassifier.ModelParameters.ClassifierType](mlsoundclassifier/modelparameters-swift.struct/classifiertype.md)
  The classifier options for a sound classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/modelparameters-swift.struct/featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](mlsoundclassifier/modelparameters-swift.struct/featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlsoundclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlsoundclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlsoundclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [MLSoundClassifier.DataSource](mlsoundclassifier/datasource.md)
  A representation of a sound-classifier dataset located in the file system or in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct)*