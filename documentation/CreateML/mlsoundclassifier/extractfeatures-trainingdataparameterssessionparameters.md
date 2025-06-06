# extractFeatures(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Begins an asynchronous session that extracts sound features from a data source of sound files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters = FeatureExtractionParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the sound feature extraction session.

#### Discussion

Use this method to reduce the training time for multiple sound classifiers that use the same training data. Use the [`MLJob`](mljob.md) instance this method returns to save the audio features as an [`MLSoundClassifier.DataSource`](mlsoundclassifier/datasource.md). Then use the audio features data source to train one or more sound classifiers.

You can also create a data source from a [`DataFrame`](https://developer.apple.com/documentation/TabularData/DataFrame) or an [`MLDataTable`](mldatatable.md) that contains audio features by using [`MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)`](mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:).md) or [`MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)`](mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:).md), respectively.

## Parameters

- `trainingData`: An   instance that contains a collection of labeled audio   files.
- `parameters`: An   instance you use to configure the feature   extraction session.
- `sessionParameters`: An   instance you use to configure the feature extraction   session.

## See Also

- [static func train(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-5hdqg.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func train(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-6z4c8.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a dictionary.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/resume(_:).md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.
- [MLSoundClassifier.FeatureExtractionParameters](mlsoundclassifier/featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))*