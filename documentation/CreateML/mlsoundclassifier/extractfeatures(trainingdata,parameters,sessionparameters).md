# extractFeatures(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

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

An [`MLJob`](../mljob.md) that represents the sound feature extraction session.

#### Discussion

Use this method to reduce the training time for multiple sound classifiers that use the same training data. Use the [`MLJob`](../mljob.md) instance this method returns to save the audio features as an [`MLSoundClassifier.DataSource`](./datasource.md). Then use the audio features data source to train one or more sound classifiers.

You can also create a data source from a [`DataFrame`](../../TabularData/dataframe.md) or an [`MLDataTable`](../mldatatable.md) that contains audio features by using [`MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)`](./datasource/featuresdataframe%28_,featurecolumn,labelcolumn,parameters%29.md) or [`MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)`](./datasource/features%28table,featurecolumn,labelcolumn,parameters%29.md), respectively.

## Parameters

- `trainingData`: An [`MLSoundClassifier.DataSource`](./datasource.md) instance that contains a collection of labeled audio files.
- `parameters`: An [`MLSoundClassifier.FeatureExtractionParameters`](./featureextractionparameters.md) instance you use to configure the feature extraction session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the feature extraction session.

## See Also

### Training a sound classifier asynchronously
- [static train(trainingData:parameters:sessionParameters:)](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.
- [MLSoundClassifier.FeatureExtractionParameters](./featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:))*